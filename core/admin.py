from django.contrib import admin
from .models import SharedSecret

@admin.register(SharedSecret)
class SharedSecretAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'expires_at', 'is_opened')
    list_filter = ('is_opened', 'expires_at')
