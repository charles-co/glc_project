from django.apps import AppConfig


class BibleConfig(AppConfig):
    name = 'bible'

    def ready(self):
        import bible.signals
