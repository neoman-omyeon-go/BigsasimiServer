from .base import *

ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': DATABASES_SELECT['postgres']
}

STATIC_ROOT = None
