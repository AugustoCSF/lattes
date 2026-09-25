"""URL configuration for lattes_web project."""
from django.urls import path

from barema_app import views

urlpatterns = [
    path("", views.upload_view, name="upload"),
    path("configurar/", views.configurar_view, name="configurar"),
    path("resultado/", views.resultado_view, name="resultado"),
    path("download/", views.download_view, name="download"),
]
