"""Index urls module."""

# Django
from django.urls import path
# Project
from .views import MainView


urlpatterns = [
    path('', MainView.as_view(), name='main'),
]
