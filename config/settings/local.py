from .base import *

ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': DATABASES_SELECT['local_postgres']
}

STATIC_ROOT = None
