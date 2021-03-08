"""Index urls module."""

# Django
from django.urls import path
# Project
from .views import main


urlpatterns = [
    path('', main, name='main'),
]
