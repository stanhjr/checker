from celery import Celery

from celery_tasks.celery_config import config
from social_checkers.social_media_checker import social_media_checker
from core.db.db_api import data_api
from email_checkers.gmail_checker import gmail_checker
from email_checkers.hotmail_checker import hotmail_check
from email_checkers.yahoo_checker import yahoo_checker

app = Celery('tasks')
config['broker_url'] = 'redis://localhost:6379'
config['result_backend'] = 'redis://localhost:6379'
app.config_from_object(config)


@app.task
def celery_email_check(email):
    """
    Checking email and save available email to database

    :return
    """
    if email.find("@hotmail.com") > 0:
        if hotmail_check(email):
            data_api.set_available_hotmail(email)
            social_media_checker(email=email)
    if email.find("@yahoo.com") > 0:
        if yahoo_checker(email=email):
            data_api.set_available_yahoo(email)
            social_media_checker(email=email)
    if email.find("@gmail.com") > 0:
        if gmail_checker(email):
            data_api.set_available_gmail(email=email)
            social_media_checker(email=email)

