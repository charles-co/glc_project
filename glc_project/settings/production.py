from .base import *
import django_heroku
from django.utils.translation import ugettext_lazy as _

DEBUG = False

ALLOWED_HOSTS = ["*.herokuapp.com"]

EMAIL_HOST = os.environ.get("MAILGUN_SMTP_SERVER", "")
EMAIL_HOST_USER     = os.environ.get("MAILGUN_SMTP_LOGIN", "")
EMAIL_HOST_PASSWORD = os.environ.get("MAILGUN_SMTP_PASSWORD", "")
EMAIL_PORT = os.environ.get("MAILGUN_SMTP_PORT", "")
# EMAIL_USE_SSL = True # Yes for Gmail
DEFAULT_FROM_EMAIL = "GLC <webmaster@localhost>"

CORS_REPLACE_HTTPS_REFERER      = True
HOST_SCHEME                     = "https://"
SECURE_PROXY_SSL_HEADER         = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT             = True
SESSION_COOKIE_SECURE           = True
CSRF_COOKIE_SECURE              = True
SECURE_HSTS_INCLUDE_SUBDOMAINS  = True
SECURE_HSTS_SECONDS             = 1000000
SECURE_FRAME_DENY               = True

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
    'LOGIN_SPLASH': '/static/images/background3.jpg',
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
        { 'type': 'free', 'label': 'Custom Link', 'url': 'http://www.google.it', 'perms': ('flatpages.add_flatpage', 'auth.change_user') },
        { 'type': 'free', 'label': 'My parent voice', 'default_open': True, 'children': [
            { 'type': 'model', 'label': 'Event', 'name': 'event', 'app': 'events' },
            { 'type': 'free', 'label': 'Another custom link', 'url': 'http://www.google.it' },
        ] },
    ),
    'ANALYTICS': {
        'CREDENTIALS': os.environ.get('GOOGLE_CREDENTIALS'),
        'VIEW_ID': os.environ.get('VIEW_ID'),
    }
}

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL ='/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

django_heroku.settings(locals(), logging=False, staticfiles=False)
