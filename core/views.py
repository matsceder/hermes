from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')  # Lägg till denna funktion

def share_text(request):
    if request.method == 'POST':
        # Placeholder: Här hanterar vi formulärdata senare
        text = request.POST.get('text')
        expiration = request.POST.get('expiration')
        return render(request, 'core/share_text.html', {'success': True})

    return render(request, 'core/share_text.html')
