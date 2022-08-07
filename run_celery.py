from celery_tasks.tasks import app


if __name__ == "__main__":
    argv = [
        'worker',
        '--loglevel=INFO',
        '--without-heartbeat',
        '--without-mingle',
        '--without-gossip',
        '--queues=email_checker'
    ]
    app.worker_main(argv)

