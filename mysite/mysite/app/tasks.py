from __future__ import absolute_import, unicode_literals
from celery import shared_task
from celery import task

@task()
def test():
    print("hello")
