"""Tests for training_sessions urls."""
from django.urls import resolve
from django.urls import reverse


def test_list_reverses() -> None:
    """It reverses sessions:list to /sessions/."""
    assert reverse("sessions:list") == "/sessions/"


def test_list_resolves() -> None:
    """It resolves /sessions/ to sessions:list."""
    assert resolve("/sessions/").view_name == "sessions:list"


def test_add_reverses() -> None:
    """It reverses sessions:add to /sessions/add."""
    assert reverse("sessions:add") == "/sessions/add"


def test_add_resolves() -> None:
    """It resolves /sessions/add to sessions:add."""
    assert resolve("/sessions/add").view_name == "sessions:add"


def test_detail_reverses() -> None:
    """It reverses sessions:detail to /sessions/<pk>."""
    assert reverse("sessions:detail", kwargs={"pk": "1"}) == "/sessions/1/"


def test_detail_resolves() -> None:
    """It resovles /sessions/slug/ to sessions:detail."""
    assert resolve("/sessions/1/").view_name == "sessions:detail"


def test_update_reverses() -> None:
    """It reverses sessions:update to /sessions/<pk>/update."""
    assert reverse("sessions:update", kwargs={"pk": "1"}) == "/sessions/1/update"


def test_edit_resolves() -> None:
    """It resolves /sessions/<pk>/update to session:update."""
    assert resolve("/sessions/1/update").view_name == "sessions:update"
