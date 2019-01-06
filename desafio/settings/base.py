"""
Django settings for desafio project.

Generated by 'django-admin startproject' using Django 2.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""
import os
import sys
from decouple import config
from os.path import abspath, basename, dirname, join, normpath

'''
    PROJECT DIRS
'''
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def base_dir_join(*args):
    return os.path.join(BASE_DIR, *args)

APPS_DIR = base_dir_join('apps')

'''
    PROJECT SECRET KEY
'''
SECRET_KEY = '&or4w@w%s253)5(&gc565p9!u91_ba!zn5g^epkwed3e9-i_4w'

'''
    PROJECT DATA FORMAT
'''
DATE_INPUT_FORMATS = ('%d-%m-%Y')

'''
    SET TRUE TO ENABLE DEBUG
'''
DEBUG = True

'''
    SET ADMINS TO ENABLE DEBUG
'''
ADMINS = (
    ('Ylgner', 'ylgner.becton@gmail.com'),
)
SITE_NAME=''
MANAGERS = ADMINS

'''
    PROJECT HOSTS
'''
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

'''
    CUSTOM AUTH
'''
AUTH_USER_MODEL = 'default.Usuario'

'''
    APLICATIONS
'''
# Application definition
DJANGO_APPS = [
    # Default Django apps:
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Admin
    'django.contrib.admin',
    'django.contrib.admindocs',
]

THIRD_PARTY_APPS = [
    'material',
    'material.frontend',
    'material.admin',
    'nested_admin',
]

# Apps specific for this project go here.
LOCAL_APPS = [
    # custom users app
    'apps.api_rest',
    'apps.default',
    'apps.message_core',
    # Your stuff: custom apps go here
]

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

'''
    URLS
'''
ROOT_URLCONF = 'desafio.urls'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [base_dir_join('templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                # 'django.template.context_processors.i18n',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ]
        },
    },
]

'''
    WSGI
'''
WSGI_APPLICATION = 'desafio.wsgi.application'

'''
    AUTHENTICATION
'''
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

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

'''
    INTERNACIONALIZATION
'''
LANGUAGE_CODE = 'pt-br'
LANGUAGES = (
 ('pt-br', ('Brasilian Portuguese')),
 ('en', ('English')),
 ('es', ('Spanish')),
)

TIME_ZONE = 'America/Recife'

USE_I18N = True
USE_L10N = True
USE_TZ = True

SITE_ID = 2

'''
    STATIC FILES
'''
STATIC_ROOT = str(base_dir_join('staticfiles'))
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    base_dir_join('static'),
)

'''
    UPLOADS MEDIA
'''
MEDIA_ROOT = str(base_dir_join('media'))
MEDIA_URL = '/media/'

'''
    LOG CONFIG
'''
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

'''
SIMPLE HISTORY
'''
INSTALLED_APPS += ['simple_history', ]
MIDDLEWARE += [
    'simple_history.middleware.HistoryRequestMiddleware',
]

'''
DJANGO REST FRAMEWORK
'''
INSTALLED_APPS += [
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    'rest_auth.registration',
    'django_filters',
    'rest_framework_swagger',
    'oauth2_provider',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.instagram',
    'allauth.socialaccount.providers.google',
]

'''
    REST FRAMEWORK
'''
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework.filters.SearchFilter',
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.CursorPagination',
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
    'PAGE_SIZE': 50
}

'''
    LOGIN
'''
API_URL = "http://127.0.0.1:8000/o/token/"

LOGIN_REDIRECT_URL = 'api/'
LOGIN_URL = '/'
ACCOUNT_EMAIL_VERIFICATION = None
ACCOUNT_LOGOUT_REDIRECT_URL = '/'
SOCIALACCOUNT_EMAIL_VERIFICATION = None
SOCIALACCOUNT_QUERY_EMAIL = True
SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        'SCOPE': ['email', 'user_birthday' ,'publish_actions','user_friends'],
        'METHOD': 'js_sdk'  # instead of 'oauth2'
  }
}
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = True

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'basic': {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header"
        }
    },
    'LOGIN_URL': 'rest_framework:login',
    'LOGOUT_URL': 'rest_framework:logout',
}

ADMIN_SITE_HEADER = "Administração"

OAUTH2_PROVIDER = {
    'SCOPES': {'read': 'Read scope', 'write': 'Write scope', 'groups': 'Access to your groups'},
    'ACCESS_TOKEN_EXPIRE_SECONDS': 60 * 60 * 24 * 180,
}

'''
EMAIL
'''
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_FROM = ''

'''
SMS
'''
SMS_FROM = 'SMS'
SMS_TOKEN = ''
CHECK_SMS = True

"""
    DJANGO_FILER
"""
INSTALLED_APPS += [
    'easy_thumbnails',
    'filer',
    'mptt',
]

THUMBNAIL_DEBUG = True
THUMBNAIL_HIGH_RESOLUTION = True

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)
FILER_CANONICAL_URL = 'sharing/'

'''
    DJANGO CORS
'''
CORS_ORIGIN_ALLOW_ALL = True