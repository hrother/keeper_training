import factory
from factory.django import DjangoModelFactory

from keeper_training.drills.models import Drill


class DrillFactory(DjangoModelFactory):

    name = factory.Faker("bs")
    description = factory.Faker("text")
    image = factory.django.ImageField()

    class Meta:
        model = Drill
