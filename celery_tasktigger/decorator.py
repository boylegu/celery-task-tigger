#
# Copyright 2016 Boyle Gu
# Licensed under The MIT License (MIT)
# http://opensource.org/licenses/MIT
#
from __future__ import absolute_import, unicode_literals
from functools import wraps

from celery_tasktigger import LoopCaptureTag, check_argument


def tigger_task(**tigger_kwargs):
    """
    Fully compatible with Celery

    :param tigger_kwargs: countdown  # Execute in x seconds (default 1 seconds )
    :param tigger_kwargs: max_times  # Max x times
    """

    def _decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            check_args = None
            try:
                check_args = check_argument(**tigger_kwargs)
                func(self, *args, **kwargs)
                raise LoopCaptureTag()
            except LoopCaptureTag as exc:
                raise self.retry(exc=exc, countdown=check_args['countdown'],
                                 max_retries=check_args['max_times'])

        return wrapper

    return _decorator
