from django.apps import AppConfig


class AuthenticationConfig(AppConfig):
    name = 'authentication'
    icon_name = 'manage_accounts'

    def ready(self):
        import authentication.signals