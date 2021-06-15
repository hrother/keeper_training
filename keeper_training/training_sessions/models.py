import datetime

from django.conf import settings
from django.db import models
from django.urls import reverse
from model_utils.models import TimeStampedModel


class TrainingSession(TimeStampedModel):
    """A training session."""

    date = models.DateField()
    coach = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    drills = models.ManyToManyField(
        "drills.Drill",
        through="training_sessions.SessionDrills",
        null=True,
        blank=True,
    )

    def get_absolute_url(self) -> str:
        return reverse("sessions:detail", kwargs={"pk": self.pk})

    def get_update_url(self) -> str:
        return reverse("sessions:update", kwargs={"pk": self.pk})

    def duration(self):
        """Total duration of session."""
        return sum(
            (drill.duration for drill in self.drills.all()), datetime.timedelta()
        )


class SessionDrills(models.Model):
    """Through model allowing for ordering."""

    session = models.ForeignKey(
        "training_sessions.TrainingSession", on_delete=models.CASCADE
    )
    drill = models.ForeignKey("drills.Drill", on_delete=models.CASCADE)
    order = models.IntegerField(default=99)

    class Meta:
        ordering = ["order"]
