from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('share-text/', views.share_text, name='share_text'),
    path("unlock/<uuid:secret_id>/<str:key>/", views.unlock_secret, name="unlock_secret"),
    path("unlock/<uuid:secret_id>/", views.unlock_secret, name="unlock_secret_manual"),
]
