from django.apps import AppConfig


class PollsConfig(AppConfig):
    """
    See:
    https://docs.djangoproject.com/en/2.2/ref/applications/#configuring-applications
    settings.INSTALLED_APPS
    """
    name = 'polls'
    verbose_name = "Polls"
