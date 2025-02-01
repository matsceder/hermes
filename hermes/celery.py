import os
from celery.schedules import crontab
from celery import Celery

# Ställ in Django-inställningarna för Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hermes.settings')

app = Celery('hermes')
app.config_from_object('django.conf:settings', namespace='CELERY')

# Auto-discover tasks från alla installerade Django-appar
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'delete-expired-secrets-daily': {
        'task': 'core.tasks.delete_expired_secrets',
        'schedule': crontab(hour=2, minute=0),  # Körs varje dag kl 02:00
    },
}

app.conf.timezone = 'Europe/Stockholm'
