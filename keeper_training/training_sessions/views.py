from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http.response import HttpResponse
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .models import TrainingSession


class TrainingSessionListView(ListView):
    model = TrainingSession
    allow_empty = True

    def get_queryset(self) -> QuerySet:
        qs = super().get_queryset().select_related("coach").prefetch_related("drills")
        qs = qs.filter(coach=self.request.user)
        return qs


class TrainingSessionCreateView(LoginRequiredMixin, CreateView):
    model = TrainingSession
    fields = ("drills",)

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.coach = self.request.user
        return super().form_valid(form)


class TrainingSessionDetailView(LoginRequiredMixin, DetailView):
    model = TrainingSession


training_session_list_view = TrainingSessionListView.as_view()
training_session_create_view = TrainingSessionCreateView.as_view()
training_session_detail_view = TrainingSessionDetailView.as_view()
