import json
from logging import info

from celery import Celery
import requests

from celery_tasks.celery_config import config
from celery.signals import task_prerun
from core.db.db_api import data_api
from core.db.models import engine
from core.schemas import EmailCheckerScraper, EmailCheckerIpQuality

app = Celery('tasks')
config['broker_url'] = 'redis://localhost:6379/5'
app.config_from_object(config)


def check_email_valid(email: str) -> bool:
    email = email.strip()
    if email.find('@gmail.com') > 0:
        return True
    if email.find('@yahoo.com') > 0:
        return True
    if email.find('@hotmail.com') > 0:
        return True
    if email.find('aol.com') > 0:
        return True
    return False


@task_prerun.connect
def on_task_init(*args, **kwargs):
    engine.dispose()


def celery_email_check(email):
    """
    Checking email and save available email to database

    :return
    """

    if not data_api.check_social(email):
        return f'This email {email} is not checked!'

    if not check_email_valid(email):
        return f'This email {email} not valid'

    headers = {
        "X-API-KEY": "38045cad-2eae-4ae0-9c39-7e1f2da9ef31"
    }

    r = requests.get(f"https://api.seon.io/SeonRestService/email-api/v2.2/{email}?include=history", headers=headers)
    result = json.loads(r.text)
    data = result.get('data')
    if not data:
        return 'not data'
    checker = EmailCheckerScraper(**data)
    if checker.domain_details.registered is not True:
        return f"{email} -> this host not registered"
    if checker.deliverable is False:
        data_api.set_checker_result(scraper=checker)
        return True
    return f"{email} -> this email not deliverable"


@app.task
def check_email(email):
    """
     Checking email and save available email to database

    :param email: str:

    :return: str
    """

    if not check_email_valid(email):
        return f'This email {email} not valid'

    if data_api.check_email(email):
        return f'This email {email} already checked'

    api_key = '3kIfZsJL2HvmIRqqTIa3vmfN0xAt9v8P'
    r = requests.get(f"https://www.ipqualityscore.com/api/json/email/{api_key}/{email}?timeout=30")
    result = json.loads(r.text)
    checker = EmailCheckerIpQuality(**result)

    if checker.domain_velocity is None:
        data_api.set_email_parse_result(email=email, available=False, incorrect=True)
        return f'This email -> {email} is not valid'

    if checker.valid is True:
        data_api.set_email_parse_result(email=email, available=False, incorrect=False)
        return f'This email -> {email} is not available'

    if checker.valid is False:
        data_api.set_email_parse_result(email=email, available=True, incorrect=False)
        info(f'This email -> {email} available')
        celery_email_check(email=email)


if __name__ == '__main__':
    print(check_email_valid('a.goeree@home.nl'))
    # print(check_email('stanhjrpower@gmail.com'))