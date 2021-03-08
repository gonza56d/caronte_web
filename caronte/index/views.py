"""Index views module."""

# Django
from django.shortcuts import render
# Project
from caronte.users.forms import SignupForm
from caronte.utils.constants.strings import CARONTE_INDEX_DESCRIPTION


def main(request):
    signup_form = SignupForm()
    return render(request, 'index/main.html', {
        'signup_form': signup_form,
        'CARONTE_INDEX_DESCRIPTION': CARONTE_INDEX_DESCRIPTION
    })
