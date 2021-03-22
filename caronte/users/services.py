"""Users business logic module."""

# Django
from django.contrib import auth
# Project
from .models import User


def signup(username, email, password, first_name, last_name):
    """Handle user signup logic."""

    user = User.objects.create_user(
        username=username,
        email=email,
        password=password,
        first_name=first_name,
        last_name=last_name
    )
    return user


def login(request, username, password):
    """Handle user login business logic."""

    if username:
        username = username.lower()

    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
    return user


def logout(request):
    auth.logout(request)
