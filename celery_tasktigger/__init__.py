"""
Handled exceptions raised by celery-task-tigger

"""
from __future__ import unicode_literals


class LoopCaptureTag(Exception):
    """ disguise a exception for cheat celery"""

    def __str__(self):
        return 'Start'


class TimesValuesError(Exception):
    """check decorator params: max_times"""

    def __str__(self):
        return "params of tigger_task: max_times, isn't exist "


def check_argument(**kwargs):
    countdown = kwargs.get('countdown', 1)  # default 1 seconds
    max_times = kwargs.get('max_times')
    if not max_times:
        raise TimesValuesError()
    elif max_times == 'forever':

        """default 77777 times .
           Please be careful! if use, don't forget revoke it"""

        max_times = 77777
    elif not isinstance(max_times, int):
        raise TypeError("max_times must int type")

    return dict(countdown=countdown, max_times=max_times)
