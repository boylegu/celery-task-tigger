from __future__ import absolute_import
from functools import wraps

from celery_tasktigger import LoopCaptureException


def tigger_task(**tigger_kwargs):
    def _decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            countdown = tigger_kwargs.get('countdown')

            try:
                func(self, *args, **kwargs)
                raise LoopCaptureException('loop')
            except Exception as exc:
                raise self.retry(exc=exc, countdown=countdown, max_retries=1000)

        return wrapper

    return _decorator
