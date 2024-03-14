from .base import *

ALLOWED_HOSTS = []

DATABASES = {
    'default': DATABASES_SELECT['local_postgres']
}

STATICFILES_DIRS = [
    STATIC_DIR
]