"""Test training_sessions models."""

import pytest
from django.urls import reverse

from keeper_training.training_sessions.models import TrainingSession

pytestmark = pytest.mark.django_db


def test_absolute_url(training_session: TrainingSession) -> None:
    """It returns the absolute url."""
    assert training_session.get_absolute_url() == reverse(
        "sessions:detail",
        kwargs={"pk": training_session.id},
    )


def test_update_url(training_session: TrainingSession) -> None:
    """It returns the update url."""
    assert training_session.get_update_url() == reverse(
        "sessions:update",
        kwargs={"pk": training_session.id},
    )
