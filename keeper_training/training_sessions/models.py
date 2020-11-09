from django.conf import settings
from django.db import models
from django.urls import reverse
from model_utils.models import TimeStampedModel


class TrainingSession(TimeStampedModel):
    """A training session."""

    coach = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    drills = models.ManyToManyField("drills.Drill")

    def get_absolute_url(self) -> str:
        return reverse("sessions:detail", kwargs={"pk": self.pk})
