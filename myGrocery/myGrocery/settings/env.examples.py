from .base import *
SECRET_KEY = 'Your Secret key here'
DEBUG = 'Boolean Value'

if DEBUG:
    INTERNAL_IPS = [
        '127.0.0.1',
    ]
    MIDDLEWARE += [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]

    ALLOWED_HOSTS = ['*']
else:
    ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}