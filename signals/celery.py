import os
from celery import Celery
from django.conf import settings
from celery.signals import task_prerun, task_postrun
import logging
logger = logging.getLogger(__name__)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'signals.settings')

app = Celery('signals')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    logger.info("\n\nRequest: {0}\n\n".format(self.request))

@task_prerun.connect()
def receiver_task_prerun(task_id, task, *args, **kwargs):
    logger.info("\n\nPre run: \n\n Task: {0}\n\n".format(task))


@task_postrun.connect()
def receiver_task_postrun(task_id, task, *args, **kwargs):
    # note that this hook runs even when there has been an exception thrown by the task
    logger.info("\n\nPost run: \n\n Task: {0}\n State: {1}\n\n".format(task, kwargs.get('state', None)))
