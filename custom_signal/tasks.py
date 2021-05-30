from celery.decorators import task

@task
def hello(msg="Hello"):
    print("Yo - {0}".format(msg))
