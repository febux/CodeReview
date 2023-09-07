import os

from celery import Celery
from celery.schedules import crontab

from .settings import CELERY_BROKER_URL

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "code_review_project.settings")

app = Celery('code_review_project', broker=CELERY_BROKER_URL, include=["code_review_project.tasks"])
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


app.conf.beat_schedule = {
    "check_new_files": {
        "task": "code_review_project.tasks.check_new_files",
        "schedule": crontab(minute="*/1"),
    },
}
