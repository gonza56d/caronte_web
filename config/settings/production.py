"""Production settings configurations."""

from .base import *


DEBUG = False

ALLOWED_HOSTS = ['caronte.pythonanywhere.com', 'localhost', '127.0.0.1', 'http://localhost:5500']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(ROOT_DIR('production.sqlite3')),
    }
}

# CORS_ALLOWED_ORIGINS = ['http://localhost:5500']

# CORS_ORIGIN_WHITELIST = ['localhost:5500']

# CORS_ALLOW_ALL_ORIGINS = True

# CORS_ALLOW_CREDENTIALS = True
