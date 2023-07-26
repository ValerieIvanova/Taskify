from django.apps import AppConfig


class ProfileappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'taskify.profileApp'

    def ready(self):
        import taskify.profileApp.signals
