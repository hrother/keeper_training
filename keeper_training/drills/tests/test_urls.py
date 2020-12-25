from django.urls import resolve
from django.urls import reverse


def test_list_reverses() -> None:
    """Reverse drills:list to /drills/."""
    assert reverse("drills:list") == "/drills/"


def test_list_resolves() -> None:
    """It resolves /drills/ to drills:list."""
    assert resolve("/drills/").view_name == "drills:list"


def test_detail_reverse() -> None:
    """Reverse drills:detail to /drills/<slug>/."""
    assert reverse("drills:detail", kwargs={"slug": "slug"}) == "/drills/slug/"


def test_detail_resolve() -> None:
    """IT resolves /drills/slug/ to drills:detail."""
    assert resolve("/drills/slug/").view_name == "drills:detail"


def test_add_reverses() -> None:
    """It reverses drills:add to /drills/add."""
    assert reverse("drills:add") == "/drills/add"


def test_add_resolves() -> None:
    """It resolves /drills/add to drills:add."""
    assert resolve("/drills/add").view_name == "drills:add"


def test_update_reverses() -> None:
    """It reverses drills:update to /drills/<slug>/update."""
    assert reverse("drills:update", kwargs={"slug": "slug"}) == "/drills/slug/update"


def test_edit_resolves() -> None:
    """It resolves /drills/<slug>/update to drills:update."""
    assert resolve("/drills/slug/update").view_name == "drills:update"
