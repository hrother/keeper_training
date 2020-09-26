from autoslug import AutoSlugField
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel


class Drill(TimeStampedModel):
    """A drill"""

    name = models.CharField(_("Name of Drill"), max_length=150)
    slug = AutoSlugField(populate_from="name")
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def get_absolute_url(self):
        """Get url for drill's detail view.

        Returns:
            str: URL for dril detail.
        """
        return reverse("drills:detail", kwargs={"slug": self.slug})


    def __str__(self) -> str:
        """String representation of a drill."""
        return str(self.slug)
