from .base import *

DEBUG = bool(os.environ.get("DEBUG"))

ALLOWED_HOSTS = ["*.herokuapp.com", "127.0.0.1",]

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER     = os.environ.get("GMAIL_EMAIL")
EMAIL_HOST_PASSWORD = os.environ.get("GMAIL_PASSWORD")
EMAIL_PORT = 465
EMAIL_USE_SSL = True # Yes for Gmail
DEFAULT_FROM_EMAIL = "GLC <ch4rles.co@gmail.com>"

CORS_REPLACE_HTTPS_REFERER      = True
HOST_SCHEME                     = "https://"
SECURE_PROXY_SSL_HEADER         = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT             = True
SESSION_COOKIE_SECURE           = True
CSRF_COOKIE_SECURE              = True
SECURE_HSTS_INCLUDE_SUBDOMAINS  = True
SECURE_HSTS_SECONDS             = 1000000
SECURE_FRAME_DENY               = True

MEDIA_URL ='/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

django_heroku.settings(locals())