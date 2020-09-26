from django.urls import resolve, reverse


def test_list_reverses() -> None:
    """Reverse drills:list to /drills/."""
    assert reverse("drills:list") == "/drills/"


def test_list_resolves() -> None:
    """It resolves /drills/ to drills:list."""
    assert resolve("/drills/").view_name == "drills:list"


def test_detail_reverse() -> None:
    """Reverse drills:detail to /drills/<slug>/."""
    assert reverse("drills:detail", kwargs={"slug": "slug"}) == f"/drills/slug/"


def test_detail_resolve() -> None:
    """IT resolves /drills/slug/ to drills:detail."""
    assert resolve(f"/drills/slug/").view_name == "drills:detail"
