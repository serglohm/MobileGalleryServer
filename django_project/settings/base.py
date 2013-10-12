import os
from local import *

TEMPLATE_DEBUG = DEBUG

PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

MEDIA_ROOT = os.path.abspath(os.path.join(PROJECT_PATH, '../static_content/media'))
STATIC_ROOT = os.path.abspath(os.path.join(PROJECT_PATH, '../static_content/static'))

MEDIA_URL = '/media/'
STATIC_URL = '/static/'


with open(os.path.join(PROJECT_PATH, 'settings', 'secret_key.txt')) as f:
    SECRET_KEY = f.read().strip()


INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'gunicorn',
    'main'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.auth.context_processors.auth',
)

STATICFILES_FINDERS = (
    'settings.staticfinders.StaticRootFinder',
    'settings.staticfinders.MediaRootFinder'
)

ROOT_URLCONF = 'settings.urls'
WSGI_APPLICATION = 'settings.wsgi.application'

LANGUAGE_CODE = 'ru-RU'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_L10N = True
USE_TZ = True

TEMPLATE_DIRS = (os.path.join(PROJECT_PATH, 'templates'),)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


AUTH_PROFILE_MODULE = 'main.UserProfile'
LOGIN_URL = '/login/'
LOGOUT_URL = '/logout/'