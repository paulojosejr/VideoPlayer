from django.urls import path
from django.conf import settings
from django.contrib import admin
from .views import CriarVideo

urlpatterns = [
    path('criar/', CriarVideo.as_view(), name='criar-video'),
]
