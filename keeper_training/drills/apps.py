from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class DrillsConfig(AppConfig):
    name = "keeper_training.drills"
    verbose_name = _("Drills")

    def ready(self):
        try:
            import keeper_training.drills.signals  # noqa F401
        except ImportError:
            pass
