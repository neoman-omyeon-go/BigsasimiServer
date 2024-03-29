from .base import *

ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': DATABASES_SELECT['sqlite3']
}

STATIC_ROOT = None