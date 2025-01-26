from django.apps import AppConfig

class PostConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'post'

    def ready(self):
        # Import Group inside ready() to ensure models are loaded
        from django.contrib.auth.models import Group

        # Create groups if they don't already exist
        Group.objects.get_or_create(name='Admin')
        Group.objects.get_or_create(name='Editor')