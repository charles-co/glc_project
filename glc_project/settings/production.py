from .base import *

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

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
MEDIA_URL ='/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

django_heroku.settings(config=locals(), staticfiles=False, logging=False)
