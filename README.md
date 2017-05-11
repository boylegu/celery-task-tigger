celery-task-tigger
====

[![release](https://img.shields.io/badge/release-0.3-blue.svg)]()
[![license](https://img.shields.io/badge/license-MIT-blue.svg)]()
[![celery](https://img.shields.io/badge/celery-3%7C4-brightgreen.svg)]()


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

Type:  ***int***

Default: 1 (seconds)

Example: 

~~~python
@app.task(bind=True)
@tigger_task(max_times='forever', countdown=3)    # each execute in 3 seconds
def add(self, x, y):
    return x + y

~~~

## How To Calling Task

~~~~python
>> from example import add
>> add.apply_async((1,2))
~~~~

you can also delayed execute task, as follow：

~~~~python
>> from example import add
>> add.apply_async((1,2), countdown=4)   # after 4 seconds, begin start task
~~~~

> About Celery Task, Please see below for details： 
> [Celery Calling-Tasks Document](http://docs.jinkan.org/docs/celery/userguide/calling.html)

## How To Stop

if you appoint `max_times='forever'` or provides the bigger values of max_times, you must stop it in programe.

~~~~python
>> result = add.apply_async((1,2))
>> result.revoke()
   or
>> from mycelery import app
>> app.control.revoke('task_id')
~~~~

> See below for details： 
> [Celery Document——FAQ](http://docs.jinkan.org/docs/celery/faq.html#can-i-cancel-the-execution-of-a-task)

## Some screenshots

![](http://i1.piimg.com/536217/1ae9af3a274de4c7.gif)

## Features

- 100％ full compatible with Celery

- the frequency of execution for task

- ...and many other stuff (o,0)


## Author

- Boyle Gu
