"""Factories for training_sessions tests."""
import factory
from factory.django import DjangoModelFactory

from keeper_training.training_sessions.models import TrainingSession
from keeper_training.users.tests.factories import UserFactory


class TrainingSessionFactory(DjangoModelFactory):
    class Meta:
        model = TrainingSession

    date = factory.Faker("date_object")
    coach = factory.SubFactory(UserFactory)

    @factory.post_generation
    def drills(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for drill in extracted:
                self.drills.add(drill)
