from django.shortcuts import render, get_object_or_404
from django.utils.timezone import now, timedelta
from .models import SharedSecret
from cryptography.fernet import Fernet
from .email_service import send_secret_email


def home(request):
    return render(request, 'core/home.html')  # Lägg till denna funktion

def share_text(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        expiration_hours = int(request.POST.get('expiration'))
        recipient_email = request.POST.get('email')

        # Skapa och kryptera hemligheten
        secret = SharedSecret.objects.create(
            encrypted_text=text,
            expires_at=now() + timedelta(hours=expiration_hours)
        )

        # Skapa en unik URL
        secret_url = f"http://127.0.0.1:8000/unlock/{secret.id}/{secret.encryption_key}/"

        # Skicka e-post med länken
        send_secret_email(recipient_email, secret_url)

        return render(request, 'core/share_text.html', {'success': True, 'link': secret_url})

    return render(request, 'core/share_text.html')

def unlock_secret(request, secret_id, key=None):
    secret = get_object_or_404(SharedSecret, id=secret_id)

    # Kontrollera om texten har löpt ut eller redan öppnats
    if secret.expires_at < now():
        return render(request, 'core/unlock.html', {'message': 'The secret has expired.'})
    if secret.is_opened:
        return render(request, 'core/unlock.html', {'message': 'The secret has already been opened.'})

    # Om nyckeln finns i URL:en, försök dekryptera direkt
    if key:
        try:
            cipher = Fernet(key.encode())
            decrypted_text = cipher.decrypt(secret.encrypted_text.encode()).decode()

            # Markera texten som öppnad
            secret.is_opened = True
            secret.save()

            return render(request, 'core/unlock.html', {'decrypted_text': decrypted_text})

        except Exception:
            return render(request, 'core/unlock.html', {'message': 'Invalid decryption key.'})

    # Om ingen nyckel skickades i URL:en, visa formulär för att mata in nyckel
    if request.method == 'POST':
        input_key = request.POST.get('key')
        try:
            cipher = Fernet(input_key.encode())
            decrypted_text = cipher.decrypt(secret.encrypted_text.encode()).decode()

            # Markera texten som öppnad
            secret.is_opened = True
            secret.save()

            return render(request, 'core/unlock.html', {'decrypted_text': decrypted_text})

        except Exception:
            return render(request, 'core/unlock.html', {'message': 'Invalid key.'})

    return render(request, 'core/unlock.html', {'secret_id': secret_id})



