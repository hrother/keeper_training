from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class TrainingSessionsConfig(AppConfig):
    name = "keeper_training.training_sessions"
    verbose_name = _("Training Sessions")

    def ready(self):
        try:
            import keeper_training.training_sessions.signals  # noqa F401
        except ImportError:
            pass
