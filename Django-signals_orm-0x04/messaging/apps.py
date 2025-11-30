from django.apps import AppConfig


class MessagingConfig(AppConfig):
    name = 'messaging'

    def ready(self):
        # Import signals to register receivers
        import messaging.signals  # noqa: F401
