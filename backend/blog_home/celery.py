import os
from celery import Celery
# from celery.schedules import timedelta,crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog_home.settings")
os.environ.setdefault("FORKED_BY_MULTIPROCESSING", "1")
app = Celery("blog_home")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks(["blogs"])