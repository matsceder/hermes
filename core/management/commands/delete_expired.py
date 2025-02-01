from django.core.management.base import BaseCommand
from core.models import SharedSecret

class Command(BaseCommand):
    help = 'Deletes all expired secrets from the database'

    def handle(self, *args, **kwargs):
        deleted_count = SharedSecret.delete_expired_secrets()
        self.stdout.write(self.style.SUCCESS(f"Deleted {deleted_count} expired secrets."))
