import factory
from factory.django import DjangoModelFactory

from keeper_training.drills.models import Drill


class DrillFactory(DjangoModelFactory):

    name = factory.Faker("bs")
    description = factory.Faker("text")
    image = factory.django.ImageField()
    duration = factory.Faker("time_delta")

    class Meta:
        model = Drill
