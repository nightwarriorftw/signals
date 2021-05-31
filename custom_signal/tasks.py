from signals.celery import Logger
from celery.decorators import task

@task
def hello_world(classroom_id, classroom_name="sexy bitch"):
    print("Yo")

@task
def world():
    print("honey singh")
    print("honey singh")
    print("honey singh")