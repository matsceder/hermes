from django.shortcuts import render
from django.utils.timezone import now, timedelta
from .models import SharedSecret

def home(request):
    return render(request, 'core/home.html')  # Lägg till denna funktion

def share_text(request):
    if request.method == 'POST':
        # Hämta formulärdata
        text = request.POST.get('text')
        expiration_hours = int(request.POST.get('expiration', 24))  # Standard 24 timmar
        expires_at = now() + timedelta(hours=expiration_hours)

        # Skapa en ny post i databasen
        secret = SharedSecret.objects.create(
            encrypted_text=text,
            expires_at=expires_at
        )

        # Generera en unik länk
        link = f"http://127.0.0.1:8000/unlock/{secret.id}/"

        # Visa länken i en bekräftelsesida
        return render(request, 'core/secret_created.html', {'link': link})

    # GET-förfrågan: Visa formuläret
    return render(request, 'core/share_text.html')
