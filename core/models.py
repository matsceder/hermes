from django.db import models
import uuid
from cryptography.fernet import Fernet

class SharedSecret(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # Unikt ID
    encrypted_text = models.TextField()  # Krypterad text
    created_at = models.DateTimeField(auto_now_add=True)  # När posten skapades
    expires_at = models.DateTimeField()  # När posten ska utgå
    is_opened = models.BooleanField(default=False)  # Status för om posten öppnats

    def save(self, *args, **kwargs):
        # Kryptera texten innan lagring (Placeholder för riktig implementation)
        if not self.encrypted_text.startswith('gAAAA'):
            key = Fernet.generate_key()
            cipher = Fernet(key)
            self.encrypted_text = cipher.encrypt(self.encrypted_text.encode()).decode()
        super().save(*args, **kwargs)

    def decrypt_text(self, key):
        # Dekryptera texten
        cipher = Fernet(key)
        return cipher.decrypt(self.encrypted_text.encode()).decode()

    def __str__(self):
        return f"SharedSecret {self.id} (Expires: {self.expires_at})"
