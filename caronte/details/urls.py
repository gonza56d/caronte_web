"""Details urls."""

# Django
from django.urls import path
# Project
from caronte.details.views import CreateDetailView


urlpatterns = [
    path('create/', CreateDetailView.as_view(), name='create'),
]
