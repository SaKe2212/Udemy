from django.apps import AppConfig


class UdemyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'udemy'

from django.apps import AppConfig

class YourAppNameConfig(AppConfig):
    name = 'udemy'

    def ready(self):
        import udemy.signals
