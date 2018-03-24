from celery import Celery

celery = Celery('tasks')
celery.config_from_object('celeryconfig')
# celery = Celery('tasks', backend='rpc', broker='amqp://user:password@127.0.0.1:5672/myvhost')


@celery.task
def add(x, y):
    print('task is running in scheduler')
    return x + y
