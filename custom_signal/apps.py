from django.apps import AppConfig


class CustomSignalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'custom_signal'


    def ready(self):
        import custom_signal.signals
