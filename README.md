celery-task-tigger
====

A controllable timing task widgets with Celery

## About

As is known to all, Celery have a already provides periodic task and it's very perfit. But, Assume this case: After my task was called, I hope it's task can  frequency of execution, and when celery task was started. 

The above case, Periodic task is hard to practice, Becacuse it's depend on celery beat. ``celery-task-tigger`` do it over simple packaging or implement for solution to do it.


## Installation

~~~python
pip install celery-task-tigger

~~~

## Useage

Assume you have aleady install celery and can do it.

### Bases

Option `max_times` is must be appoint.

~~~python
from celery_tasktigger.decorator import tigger_task

@app.task(bind=True)
@tigger_task(max_times='forever')    # forever is expressed unlimited time
def add(self, x, y):
    return x + y

~~~

### max_times

Option `max_times`: The maximum number of execute the task times.

Type： ***int***

> Note: The value ***'forever'*** is expressed unlimited time. 

Example: 

~~~python
@app.task(bind=True)
@tigger_task(max_times=3)    # after execute 3 times, raise an exception
def add(self, x, y):
    return x + y

~~~

### countdown

Option `countdown`: You can also provide the countdown argument to execute.

Example: 

~~~python
@app.task(bind=True)
@tigger_task(max_times='forever', countdown=3)    # execute in 3 seconds
def add(self, x, y):
    return x + y

~~~

## How To Run



## More Example

## Features

- 100％ full compatible with Celery

- the frequency of execution for task

- ...and many other stuff (o,0)


## Author

- Boyle Gu
