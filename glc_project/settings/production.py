from .base import *
# import django_heroku
from django.utils.translation import ugettext_lazy as _

DEBUG = False

ALLOWED_HOSTS = ["*.herokuapp.com", "164.90.139.70", "localhost"]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
#EMAIL_BACKEND = 'django_ses.SESBackend'

AWS_SES_REGION_NAME = 'us-east-2'
AWS_SES_REGION_ENDPOINT = 'email.us-east-2.amazonaws.com'

EMAIL_HOST = os.environ.get("AWS_SMTP_SERVER", "")
EMAIL_HOST_USER     = os.environ.get("AWS_SMTP_LOGIN", "")
EMAIL_HOST_PASSWORD = os.environ.get("AWS_SMTP_PASSWORD", "")
EMAIL_PORT = os.environ.get("AWS_SMTP_PORT", "")
EMAIL_USE_TLS = True
# DEFAULT_FROM_EMAIL = "GLC <webmaster@localhost>"

CORS_REPLACE_HTTPS_REFERER      = False
HOST_SCHEME                     = "http://"
SECURE_PROXY_SSL_HEADER         = None
SECURE_SSL_REDIRECT             = False
SESSION_COOKIE_SECURE           = False
CSRF_COOKIE_SECURE              = False
SECURE_HSTS_SECONDS             = None
SECURE_HSTS_INCLUDE_SUBDOMAINS  = False
SECURE_FRAME_DENY               = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get("POSTGRES_NAME"),
        'USER': os.environ.get("POSTGRES_USER"),
        'PASSWORD': os.environ.get("POSTGRES_PWD"),
        'HOST': 'localhost',
        'PORT': '',
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': ('%(asctime)s [%(process)d] [%(levelname)s] '
                       'pathname=%(pathname)s lineno=%(lineno)s '
                       'funcname=%(funcName)s %(message)s'),
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        }
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    }
}

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_STATIC_LOCATION = 'static'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_STATIC_LOCATION)
STATICFILES_STORAGE = 'glc_project.storage_backends.StaticStorage'

AWS_PUBLIC_MEDIA_LOCATION = 'media/public'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_PUBLIC_MEDIA_LOCATION}/'
DEFAULT_FILE_STORAGE = 'glc_project.storage_backends.PublicMediaStorage'

BATON = {
    'SITE_HEADER': 'GLC',
    'SITE_TITLE': 'GLC',
    'INDEX_TITLE': 'GLC administration',
    'SUPPORT_HREF': 'https://google.com',
    'COPYRIGHT': 'copyright © 2020 <a href="https://www.google.com">Charles</a>', # noqa
    'POWERED_BY': '<a href="https://www.google.com">Charles</a>',
    'CONFIRM_UNSAVED_CHANGES': True,
    'SHOW_MULTIPART_UPLOADING': True,
    'ENABLE_IMAGES_PREVIEW': True,
    'CHANGELIST_FILTERS_IN_MODAL': True,
    'CHANGELIST_FILTERS_ALWAYS_OPEN': False,
    'CHANGELIST_FILTERS_FORM': True,
    'MENU_ALWAYS_COLLAPSED': False,
    'MENU_TITLE': 'Navigation',
    'MESSAGES_TOASTS': True,
    'GRAVATAR_DEFAULT_IMG': 'retro',
    'LOGIN_SPLASH': 'https://%s/%s/images/background.jpg' % (AWS_S3_CUSTOM_DOMAIN, AWS_STATIC_LOCATION),
    'MENU': (
        { 'type': 'title', 'label': 'Authentication', 'apps': ('auth', ) },
        {
            'type': 'app',
            'name': 'auth',
            'label': 'Authentication',
            'icon': 'fa fa-lock',
            'models': (
                {
                    'name': 'group',
                    'label': 'Groups'
                },
            )
        },
        { 'type': 'title', 'label': 'Users', 'apps': ('authentication', ) },
        {
            'type': 'app',
            'name': 'authentication',
            'label': 'Users & Profiles',
            'icon': 'fa fa-user',
            'models': (
                {
                    'name': 'user',
                    'label': 'Users'
                },
                {
                    'name': 'profile',
                    'label': 'Profiles'
                },
            )
        },
        { 'type': 'title', 'label': 'Bible', 'apps': ('bible', ) },
        {
            'type': 'app',
            'name': 'bible',
            'label': 'Bible',
            'icon': 'fa fa-bible',
            'models': (
                {
                    'name': 'todaysverse',
                    'label': 'Todays Verse'
                },
            )
        },
        { 'type': 'title', 'label': 'Events', 'apps': ('events', ) },
        {
            'type': 'app',
            'name': 'events',
            'label': 'Events',
            'icon': 'fa fa-church',
            'models': (
                {
                    'name': 'event',
                    'label': 'Events'
                },
            )
        },
        { 'type': 'title', 'label': 'Contents', 'apps': ('contents', ) },
        {
            'type': 'app',
            'name': 'contents',
            'label': 'Contents',
            'icon': 'fa fa-folder-plus',
            'models': (
                {
                    'name': 'audio',
                    'label': 'Audio'
                },
                {
                    'name': 'video',
                    'label': 'Video'
                },
                {
                    'name': 'podcast',
                    'label': 'Podcast'
                },
                {
                    'name': 'tv',
                    'label': 'TV'
                },
            )
        },
    ),
    'ANALYTICS': {
        'CREDENTIALS': os.path.join('google-credentials.json'),
        'VIEW_ID': os.environ.get('VIEW_ID'),
    }
}

# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# MEDIA_URL ='/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# django_heroku.settings(locals(), logging=False, staticfiles=False)