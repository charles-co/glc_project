from .base import *

DEBUG = True

ALLOWED_HOSTS = ['glc-project', 'localhost',  '192.168.43.184', '127.0.0.1', '172.20.10.4', 'glc-project.herokuapp.com']

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
}

# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = (
   os.path.join(BASE_DIR, 'static'),
)

MEDIA_URL ='/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')