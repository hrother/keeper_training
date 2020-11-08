import pytest
from django.urls.base import reverse

from keeper_training.drills.models import Drill

pytestmark = pytest.mark.django_db


def test_absolute_url(drill: Drill) -> None:
    """It returns the absolute url."""
    assert drill.get_absolute_url() == reverse(
        "drills:detail", kwargs={"slug": drill.slug}
    )


def test_str(drill: Drill) -> None:
    """It uses slug as its str representation."""
    assert str(drill) == str(drill.slug)


def test_image_url(drill: Drill) -> None:
    """It gets the image url."""
    assert drill.image_url == "/media/example.jpg"


def test_image_url_is_none_when_there_is_no_image(drill: Drill) -> None:
    """It is none when there is no image."""
    drill.image = None
    assert drill.image_url is None
