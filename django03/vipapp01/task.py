import time
from celery import task

@task
def sayhello():
    print('say')
    time.sleep(5)
    print('hello')
