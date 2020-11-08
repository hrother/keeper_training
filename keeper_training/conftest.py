import pytest

from keeper_training.drills.models import Drill
from keeper_training.drills.tests.factories import DrillFactory
from keeper_training.users.models import User
from keeper_training.users.tests.factories import UserFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user() -> User:
    return UserFactory()


@pytest.fixture
def drill() -> Drill:
    return DrillFactory()
