config = {
    'imports': ('celery_tasks.tasks',),
    'database_engine_options': {'echo': False},
    'worker_concurrency': 4,
    'task_acks_late': True,
    'task_annotations': {
        # 'celery_tasks.tasks.celery_email_check': {
        #     'rate_limit': '200/m',
        #     'queue': 'email_checker'
        # },
        'celery_tasks.tasks.check_email': {
            'rate_limit': '200/m',
            'queue': 'email_checker'
        },

    },
    'accept_content': ['json', 'application/x-python-serialize'],
    'task_serializer': 'json',
    'result_serializer': 'json',
    'event_serializer': 'json',
    'result_expires': 7200,
    'task_compression': 'gzip',
    'result_compression': 'gzip',
    'task_default_queue': 'email_checker',
    'redis_max_connections': 2,
    'broker_transport_options': {
        'max_connections': 2
    },
    'broker_pool_limit': 2
}