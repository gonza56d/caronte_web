# Django
from django.contrib.auth.views import LoginView
from django.urls import path
# Project
from .views import LoginView, SignupView


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
]
