from celery_tasks.tasks import app


if __name__ == "__main__":
    argv = [
        'worker',
        '--loglevel=DEBUG',
        '--queues=email_checker'
    ]
    app.worker_main(argv)

