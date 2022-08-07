from celery_tasks.tasks import app


if __name__ == "__main__":
    argv = [
        'worker',
        '-B',
        '--loglevel=INFO',
        '--without-heartbeat',
        '--without-mingle',
        '--without-gossip',
        '--queues=email_checker'
    ]
    app.worker_main(argv)

