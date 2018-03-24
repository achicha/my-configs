from celery.schedules import crontab


BROKER_URL = 'amqp://user:password@127.0.0.1:5672/myvhost'
CELERY_RESULT_BACKEND = 'rpc'

CELERYBEAT_SCHEDULE = {
    'every-minute': {
        'task': 'tasks.add',
        'schedule': crontab(minute='*/1'),
        'args': (1, 2),
        },
    }

