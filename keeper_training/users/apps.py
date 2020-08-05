from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "keeper_training.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import keeper_training.users.signals  # noqa F401
        except ImportError:
            pass
