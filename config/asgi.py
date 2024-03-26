import os

from django.core.wsgi import get_wsgi_application

if (os.environ.get('_HOW') == 'prod'):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.prod')
    print('prod')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')
    print('local')
    
application = get_wsgi_application()
