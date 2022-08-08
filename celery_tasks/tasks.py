import json

from celery import Celery
import requests

from celery_tasks.celery_config import config
from celery.signals import task_prerun
from core.db.db_api import data_api
from core.db.models import engine
from core.schemas import EmailCheckerScraper

app = Celery('tasks')
config['broker_url'] = 'redis://localhost:6379'
app.config_from_object(config)


@task_prerun.connect
def on_task_init(*args, **kwargs):
    engine.dispose()


@app.task
def celery_email_check(email):
    """
    Checking email and save available email to database

    :return
    """
    headers = {
        "X-API-KEY": "38045cad-2eae-4ae0-9c39-7e1f2da9ef31"
    }

    r = requests.get(f"https://api.seon.io/SeonRestService/email-api/v2.2/{email}?include=history", headers=headers)
    result = json.loads(r.text)
    data = result.get('data')
    if not data:
        return 'not data'
    checker = EmailCheckerScraper(**data)
    if checker.deliverable is not True:
        data_api.set_checker_result(scraper=checker)
        return True
    return f"{email} -> this email not deliverable"





