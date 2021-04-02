"""Test settings configurations."""

from .base import *


DEBUG = False

# Cache
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': ''
    }
}

# Databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(ROOT_DIR('tests.sqlite3')),
    }
}

# Password hasher
PASSWORD_HASHERS = ['django.contrib.auth.hashers.MD5PasswordHasher']
