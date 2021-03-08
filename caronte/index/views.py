"""Index views module."""

# Django
from django.shortcuts import render


def main(request):

    return render(request, 'index/main.html', {})
