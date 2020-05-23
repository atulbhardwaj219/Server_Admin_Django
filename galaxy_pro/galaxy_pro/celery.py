import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'galaxy_pro.settings')

app = Celery('galaxy_pro')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.config_from_object('django.conf:settings', namespace='q1')
app.autodiscover_tasks()
