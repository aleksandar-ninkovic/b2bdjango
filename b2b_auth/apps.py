from django.apps import AppConfig

class B2BAuthConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'b2b_auth'

    def ready(self):
        import b2b_auth.signals