from .base import *

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': DATABASES_SELECT['postgres']
}

DEBUG = False

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATICFILES_DIRS = []