from django.apps import AppConfig


class AuthenticationConfig(AppConfig):
    name = 'authentication'
    icon_name = 'person'

    def ready(self):
        import authentication.signals