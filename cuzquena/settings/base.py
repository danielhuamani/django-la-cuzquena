# coding=utf-8
import os
from cuzquena.util import get_env


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ENV = get_env(BASE_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

EMAIL_HOST = ENV.get('EMAIL_HOST', 'bbdd')
EMAIL_HOST_USER = ENV.get('EMAIL_HOST_USER', 'bbdd')
EMAIL_HOST_PASSWORD = ENV.get('EMAIL_HOST_PASSWORD', 'bbdd')
DEFAULT_FROM_EMAIL = ENV.get('DEFAULT_FROM_EMAIL', 'bbdd')
SERVER_EMAIL = ENV.get('SERVER_EMAIL', 'bbdd')
EMAIL_PORT = 587
EMAIL_USE_TLS = True


SECRET_KEY = ENV.get('SECRET_KEY', 'bbdd')
URL_SITE = ENV.get('URL_SITE', 'bbdd')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ()


DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
]

THIRD_PARTY_APPS = [
    "geoposition",
    'admin_reorder',
    'django_summernote',
    'easy_thumbnails',
    'filebrowser',
]


LOCAL_APPS = [
    "my_apps.web",
    "my_apps.seo"
]

INSTALLED_APPS = THIRD_PARTY_APPS + DJANGO_APPS + LOCAL_APPS
ROOT_URLCONF = 'cuzquena.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                "django.template.context_processors.static",
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'my_apps.web.processors.processors_site'
            ],
        },
    },
]

MIDDLEWARE_CLASSES = [
    'admin_reorder.middleware.ModelAdminReorder',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


WSGI_APPLICATION = 'cuzquena.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': ENV.get('DB_NAME', 'bbdd'),
        'USER': ENV.get('DB_USER'),
        'PASSWORD': ENV.get('DB_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '',
        'CONN_MAX_AGE': None,
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'es-pe'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
# LOGIN_URL = "/"
GEOPOSITION_GOOGLE_MAPS_API_KEY = 'AIzaSyAxYmorvw6JL6mAaUZKo3xxIdXyjzzfvF4'

ADMIN_REORDER = (
    # Keep original label and models
    # 'sites',

    # Rename app
    {'app': 'auth', 'label': u'AUTENTICACIÓN Y AUTORIZACIÓN'},
    {'app': 'web', 'label': u'Configuracion', 'models': (
        {'model': 'web.Configuracion', 'label': 'Configuracion del Sitio'},

    )},
    {'app': 'web', 'label': u'Home', 'models': (
        {'model': 'web.HomeBanner', 'label': 'Banner'},
        {'model': 'web.Home', 'label': 'Contenido'},
    )},
    {'app': 'web', 'label': u'Nosotros', 'models': (
        {'model': 'web.Nosotros', 'label': u'Nosotros'},
        {'model': 'web.Valores', 'label': u'Valores'},

    )},
    {'app': 'web', 'label': u'Servicios', 'models': (
        {'model': 'web.Servicios', 'label': u'Servicios Banner'},
        {'model': 'web.NuestrosServicios', 'label': u'Nuestros Servicios'},

    )},
    {'app': 'web', 'label': u'Vehiculos', 'models': (
        {'model': 'web.VehiculoBanner', 'label': u'Banner'},
        {'model': 'web.Vehiculos', 'label': u'Vehiculos'},


    )},
    {'app': 'web', 'label': u'Contacto', 'models': (
        {'model': 'web.ContactoBanner', 'label': u'Banner'},


    )},
    {'app': 'web', 'label': u'Formularios', 'models': (
        {'model': 'web.Contacto', 'label': u'Contacto'},
        {'model': 'web.MovilizarEmpresa', 'label': u'Movilizar a tu Empresa'},

    )},
    {'app': 'seo', 'label': u'SEO', 'models': (
        {'model': 'web.SEO', 'label': u'SEO'},


    )},
    # Reorder app models

    # models with custom name

)
FILEBROWSER_MAX_UPLOAD_SIZE = 26214400  # 25 MB
FILEBROWSER_NORMALIZE_FILENAME = True
FILEBROWSER_OVERWRITE_EXISTING = False
FILEBROWSER_LIST_PER_PAGE = 25

FILEBROWSER_SHOW_PLACEHOLDER = True
FILEBROWSER_PLACEHOLDER = 'no-disponible/no-disponible.png'
FILEBROWSER_EXTENSIONS = {
    'Folder': [''],
    'Image': ['.jpg', '.jpeg', '.gif', '.png', '.tif', '.tiff'],
    'Document': ['.pdf', '.doc', '.rtf', '.txt', '.xls', '.csv', '.swf'],
    'Video': ['.mov', '.wmv', '.mpeg', '.mpg', '.avi'],
    'Audio': ['.mp3', '.mp4', '.wav', '.aiff', '.midi', '.m4p']
}

FILEBROWSER_SELECT_FORMATS = {
    'file': ['Folder', 'Image', 'Document', 'Video', 'Audio'],
    'image': ['Image'],
    'document': ['Document'],
    'media': ['Video', 'Audio'],
}
FILEBROWSER_SHOW_IN_DASHBOARD = False
