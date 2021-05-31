import os
from celery import Celery
from django.conf import settings
from celery.signals import task_prerun, task_postrun,  task_received
import logging
logger = logging.getLogger(__name__)
from celery import Task

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'signals.settings')

app = Celery('signals')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    logger.info("\n\nRequest: {0}\n\n".format(self.request))


@task_prerun.connect
def receiver_task_prerun(task_id, task, *args, **kwargs):
    logger.info(
        "\n" * 6
        + "#" * 50
        + "\nPrerun Debugs logs (Task: %s):\nArguments: %s\nTaskId: %s\n"
        + "#" * 50
        + "\n" * 6,
        task.__qualname__,
        task_id,
        kwargs.get("sender").request.args,
    )


@task_postrun.connect
def receiver_task_postrun(task_id, task, retval, state, *args, **kwargs):
    logger.info(
        "\n" * 6
        + "#" * 50
        + "\nPostrun Debugs logs (Task: %s):\nTaskId: %s\nArguments: %s\nReturn value: %s\nState: %s\n"
        + "#" * 50
        + "\n" * 6,
        task.__qualname__,
        task_id,
        kwargs.get("sender").request.args,
        retval,
        state
    )
