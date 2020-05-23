import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'galaxypro.settings')

app = Celery('galaxypro')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.config_from_object('django.conf:settings', namespace='q1')
app.autodiscover_tasks()