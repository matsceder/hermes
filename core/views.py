from django.shortcuts import render, get_object_or_404
from django.utils.timezone import now, timedelta
from .models import SharedSecret
from cryptography.fernet import Fernet


def home(request):
    return render(request, 'core/home.html')  # Lägg till denna funktion

def share_text(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        expiration_hours = int(request.POST.get('expiration', 24))  # Standard 24h
        expires_at = now() + timedelta(hours=expiration_hours)

        secret = SharedSecret.objects.create(
            encrypted_text=text,
            expires_at=expires_at
        )

        link = f"http://127.0.0.1:8000/unlock/{secret.id}/"
        key = secret.encryption_key

        return render(request, 'core/secret_created.html', {'link': link, 'key': key})

    return render(request, 'core/share_text.html')


def unlock_secret(request, secret_id):
    if request.method == 'POST':
        # Hämta nyckel från formuläret
        input_key = request.POST.get('key')

        # Hämta hemligheten från databasen
        secret = get_object_or_404(SharedSecret, id=secret_id)

        # Kontrollera om texten har löpt ut eller redan öppnats
        if secret.expires_at < now():
            return render(request, 'core/unlock_failed.html', {'message': 'The secret has expired.'})
        if secret.is_opened:
            return render(request, 'core/unlock_failed.html', {'message': 'The secret has already been opened.'})

        # Försök att dekryptera texten
        try:
            cipher = Fernet(input_key.encode())
            decrypted_text = cipher.decrypt(secret.encrypted_text.encode()).decode()

            # Markera texten som öppnad
            secret.is_opened = True
            secret.save()

            # Visa den dekrypterade texten
            return render(request, 'core/unlock_success.html', {'text': decrypted_text})

        except Exception:
            return render(request, 'core/unlock_failed.html', {'message': 'Invalid key.'})

    return render(request, 'core/unlock_form.html', {'secret_id': secret_id})


