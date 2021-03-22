import pytest
from django.test import RequestFactory

from keeper_training.drills.models import Drill
from keeper_training.drills.tests.factories import DrillFactory
from keeper_training.training_sessions.models import SessionDrills
from keeper_training.training_sessions.models import TrainingSession
from keeper_training.training_sessions.tests.factories import TrainingSessionFactory
from keeper_training.training_sessions.views import training_session_create_view
from keeper_training.training_sessions.views import training_session_detail_view
from keeper_training.training_sessions.views import training_session_list_view
from keeper_training.training_sessions.views import training_session_update_view
from keeper_training.users.models import User
from keeper_training.users.tests.factories import UserFactory

pytestmark = pytest.mark.django_db


class TestTrainingSessionView:
    def test_show_sessions_of_user(self, user: User, rf: RequestFactory):
        _ = TrainingSessionFactory(coach=UserFactory())
        session = TrainingSessionFactory(coach=user)
        request = rf.get("/fake-url/")
        request.user = user
        training_session_list_view.request = request

        response = training_session_list_view(request)
        assert session in response.context_data["trainingsession_list"]


class TestTrainingSessionCreateView:
    def test_sets_user_as_coach(
        self, user: User, rf: RequestFactory, drill: Drill
    ) -> None:
        request = rf.post(
            "/fake-url/", data={"drills": [drill.id], "date": "2020-12-28"}
        )
        request.user = user
        training_session_create_view.request = request

        response = training_session_create_view(request)

        assert response.status_code == 302

        session = TrainingSession.objects.first()
        assert session.coach == user


class TestTrainingSessionUpdateView:
    def test_updates_session(
        self, user: User, rf: RequestFactory, drill: Drill
    ) -> None:
        session = TrainingSessionFactory(coach=user, drills=[drill])
        new_drill = DrillFactory()
        request = rf.post(
            "/fake-url/",
            data={"drills": [drill.id, new_drill.id], "date": session.date},
        )
        request.user = user
        training_session_update_view.request = request

        response = training_session_update_view(request, pk=session.pk)

        assert response.status_code == 302

        session.refresh_from_db()
        assert new_drill in session.drills.all()


class TestTrainingSessionDetailView:
    def test_contains_ordered_drills(self, user: User, rf: RequestFactory) -> None:
        session = TrainingSessionFactory(coach=user)
        sd2 = SessionDrills.objects.create(
            session=session, drill=DrillFactory(name="D2"), order=2
        )
        sd1 = SessionDrills.objects.create(
            session=session, drill=DrillFactory(name="D1"), order=1
        )
        sd3 = SessionDrills.objects.create(
            session=session, drill=DrillFactory(name="D3"), order=3
        )
        request = rf.get("/fake-url/", pk=session.pk)
        request.user = user
        training_session_detail_view.request = request

        response = training_session_detail_view(request, pk=session.pk)

        assert response.status_code == 200
        assert response.context_data["ordered_drills"] == [
            sd1.drill,
            sd2.drill,
            sd3.drill,
        ]
