# Django
from django.urls import path
# Project
from caronte.periods.views import CreatePeriodView


urlpatterns = [
    path('create/', CreatePeriodView.as_view(), name='create'),
]
