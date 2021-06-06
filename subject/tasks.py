from celery.decorators import task

@task
def add(x, y):
    return x+y


@task
def hello():
    print("\n\n Simple is the new sexy \n\n")
