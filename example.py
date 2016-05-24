from celery import Celery

from celery_tasktigger.decorator import tigger_task

app = Celery('example', backend='amqp', broker='amqp://127.0.0.1:5672//')

app.conf.update(
    CELERY_ACCEPT_CONTENT=['json'],
    CELERY_TASK_SERIALIZER='json',
    CELERY_RESULT_SERIALIZER='json',
    CELERY_RESULT_BACKEND='amqp',
)


@app.task(bind=True)
@tigger_task(countdown=3)
def add(x, y):
    return x + y