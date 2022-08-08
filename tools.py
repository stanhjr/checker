import json

from core.db.db_api import data_api
from celery_tasks.tasks import celery_email_check


def save_results() -> bool:
    """
    Writes the data received from the database to a text file

    :return: bool
    """
    with open("files/report.txt", "w") as f:
        for row in data_api.get_results():
            email_ = row.pop("email")
            f.writelines([email_, '   ', json.dumps(row)])
            f.writelines("\n")
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
            celery_email_check.apply_async(kwargs=dict(email=email))
            if not email:
                break


if __name__ == '__main__':
    # celery_email_check.delay("stanhjrpower@gmail.com")
    # start_checker_email()
    save_results()
