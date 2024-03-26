from .base import *

ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': DATABASES_SELECT['postgres']
}

STATICFILES_DIRS = [
    STATIC_DIR
]