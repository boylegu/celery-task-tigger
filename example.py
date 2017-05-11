from __future__ import unicode_literals

from celery import Celery

from celery_tasktigger.decorator import tigger_task

app = Celery('example', backend='amqp', broker='amqp://127.0.0.1:5672//')

#  upgrade celery 4.0
app.conf.update(
    result_backend='amqp',
    result_expires=18000,  # 5 hours.
)


# celery -A example worker -l info
@app.task(bind=True)
@tigger_task(max_times='forever', countdown=3)
def add(self, x, y):
    return x + y
