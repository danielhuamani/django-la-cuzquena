from .base import *


DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1"]


INSTALLED_APPS += (
    'debug_toolbar',
)
# Static and Media files
STATIC_ROOT = ''
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
