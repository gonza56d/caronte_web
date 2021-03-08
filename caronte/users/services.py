"""Users business logic module."""

# Django
from django.contrib.auth import authenticate
# Project
from .models import User


def signup(username, email, password, first_name, last_name):
    """Handle user signup business logic."""

    user = User.objects.create_user(
        username=username,
        email=email,
        password=password,
        first_name=first_name,
        last_name=last_name
    )
    return user


def login(username, password):
    """Handle user login business logic."""

    if username:
        username = username.lower()

    return authenticate(username=username, password=password)
