"""Index views module."""

# Django
from django.shortcuts import render
# Project
from caronte.users.forms import SignupForm


def main(request):
    signup_form = SignupForm()
    return render(request, 'index/main.html', {'signup_form': signup_form})
