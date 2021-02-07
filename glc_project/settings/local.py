from .base import *

DEBUG = True

ALLOWED_HOSTS = ['glc-project', 'localhost',  '192.168.43.184', '127.0.0.1', '172.20.10.4']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER     = os.environ.get("GMAIL_EMAIL")
EMAIL_HOST_PASSWORD = os.environ.get("GMAIL_PASSWORD")
EMAIL_PORT = 465
EMAIL_USE_SSL = True # Yes for Gmail
DEFAULT_FROM_EMAIL = "GLC <ch4rles.co@gmail.com>"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'glc_project_db',
        'USER': 'postgres',
        'PASSWORD': os.environ.get("POSTGRES_PWD"),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

CORS_REPLACE_HTTPS_REFERER      = False
HOST_SCHEME                     = "http://"
SECURE_PROXY_SSL_HEADER         = None
SECURE_SSL_REDIRECT             = False
SESSION_COOKIE_SECURE           = False
CSRF_COOKIE_SECURE              = False
SECURE_HSTS_SECONDS             = None
SECURE_HSTS_INCLUDE_SUBDOMAINS  = False
SECURE_FRAME_DENY               = False

MEDIA_URL ='/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')