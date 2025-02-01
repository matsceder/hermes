from celery import shared_task
from core.models import SharedSecret

@shared_task
def delete_expired_secrets():
    deleted_count = SharedSecret.delete_expired_secrets()
    return f"Deleted {deleted_count} expired secrets."
