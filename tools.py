from core.db.db_api import data_api
from celery_tasks.tasks import celery_email_check


def save_results() -> bool:
    """
    Writes the data received from the database to a text file

    :return:
    """
    with open("files/report.txt", "w") as f:
        for model in data_api.get_emails():
            result_record = model.email
            if model.instagram_check:
                result_record += ' instagram'
            if model.spotify_check:
                result_record += ' spotify'
            if model.pinterest_check:
                result_record += ' pinterest'
            if model.tumblr_check:
                result_record += ' tumblr'
            if model.last_fm_check:
                result_record += ' last_fm'
            f.writelines(result_record + "\n")
    return True


def start_checker_email():
    """
    Reads emails line by line from a text file and runs celery tasks

    :return:
    """
    with open('files/db.txt', 'r') as f:
        while True:
            email = f.readline()
            email = email.replace("\n", "")
            email = email.replace("\t", "")
            email = email.replace(" ", "")
            if email.find("@hotmail.com") > 0 or email.find("@yahoo.com") > 0 or email.find("@gmail.com") > 0:
                # celery_email_check.apply_async(kwargs=dict(email=email))
                celery_email_check.delay(email)
            if not email:
                break
    return
