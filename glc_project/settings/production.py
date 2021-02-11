from .base import *
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

MEDIA_URL ='/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

django_heroku.settings(locals())

# MATERIAL_ADMIN_SITE = {
#     'HEADER':  _('GLC'),  # Admin site header
#     'TITLE':  _('GLC'),  # Admin site title
#     'FAVICON':  'image/church.png',  # Admin site favicon (path to static should be specified)
#     'MAIN_BG_COLOR':  '#F15922',  # Admin site main color, css color should be specified
#     'MAIN_HOVER_COLOR':  '#FFC50C',  # Admin site main hover color, css color should be specified
#     'PROFILE_PICTURE':  'image/logo.jpg',  # Admin site profile picture (path to static should be specified)
#     'PROFILE_BG':  'image/background3.jpg',  # Admin site profile background (path to static should be specified)
#     'LOGIN_LOGO':  'image/logo.jpg',  # Admin site logo on login page (path to static should be specified)
#     'LOGOUT_BG':  'image/background.jpeg',  # Admin site background on login/logout pages (path to static should be specified)
#     'SHOW_THEMES':  True,  #  Show default admin themes button
#     'TRAY_REVERSE': False,  # Hide object-tools and additional-submit-line by default
#     'NAVBAR_REVERSE': False,  # Hide side navbar by default
#     'SHOW_COUNTS': True, # Show instances counts for each model
#     'APP_ICONS': {  # Set icons for applications(lowercase), including 3rd party apps, {'application_name': 'material_icon_name', ...}
#         'authentication_and_authorization': 'verified',
#     },
#     'MODEL_ICONS': {  # Set icons for models(lowercase), including 3rd party models, {'model_name': 'material_icon_name', ...}
#         'user': 'account_circle',
#         'profile': 'person',
#         'group': 'groups',

#     }
# }
