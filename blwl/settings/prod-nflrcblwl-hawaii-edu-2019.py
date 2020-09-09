# prod.py
from .base import *

SECRET_KEY = '5$xm@4qd_4%fxafo**fmbgm*^_%^fbyrz$1ge+&*!%jg+(s60c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*', 'www.nflrc.hawaii.edu', 'nflrc.lll.hawaii.edu', 'nflrc.hawaii.edu']

ADMINS = [('NFLRC SYS ADMIN', 'rmedina@hawaii.edu')]
'''DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'nflrc-blwl-prod',
        'USER': 'nflrcpydbuser',
        'PASSWORD': 'mA5zuN0sT3',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# MEDIA_URL = '/media/'
# MEDIA_ROOT =  'media/nflrc/')
STATIC_ROOT = '/web/static/nflrc-blwl/'
STATIC_URL = '/static/nflrc-blwl/'

SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'HhAT_dlWTREbiuC3J8mEbH6f'
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '557584999209-rsobv5c0ff4tdifnin25bma2sgg5l474.apps.googleusercontent.com' # This is the Client ID (not a key)
SOCIAL_AUTH_INACTIVE_USER_URL = '/blended/inactive-user/'
SOCIAL_AUTH_LOGIN_ERROR_URL = '/blended/login-forbidden/'

LOGIN_URL ='/blended/login/google-oauth2'
LOGIN_REDIRECT_URL = '/blended/'

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'llcit@hawaii.edu'
EMAIL_HOST_PASSWORD = 'mo161tech'
EMAIL_PORT = 587
SERVER_EMAIL = 'llcit@hawaii.edu'
