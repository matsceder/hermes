from django.db import models
import uuid
from cryptography.fernet import Fernet

class SharedSecret(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    encrypted_text = models.TextField()
    encryption_key = models.TextField()  # Nytt fält för att lagra nyckeln
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    is_opened = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.encryption_key:
            self.encryption_key = Fernet.generate_key().decode()
        cipher = Fernet(self.encryption_key.encode())
        self.encrypted_text = cipher.encrypt(self.encrypted_text.encode()).decode()
        super().save(*args, **kwargs)

    def decrypt_text(self):
        cipher = Fernet(self.encryption_key.encode())
        return cipher.decrypt(self.encrypted_text.encode()).decode()

    def __str__(self):
        return f"SharedSecret {self.id} (Expires: {self.expires_at})"
