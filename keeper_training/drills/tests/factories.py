import factory
from factory.django import DjangoModelFactory

from keeper_training.drills.models import Drill


class DrillFactory(DjangoModelFactory):

    name = factory.Faker("bs")
    description = factory.Faker("text")

    class Meta:
        model = Drill
