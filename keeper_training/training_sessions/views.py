from typing import Any
from typing import Dict

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http.response import HttpResponse
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView

from .models import TrainingSession


class TrainingSessionListView(LoginRequiredMixin, ListView):
    model = TrainingSession
    allow_empty = True

    def get_queryset(self) -> QuerySet:
        qs = super().get_queryset().select_related("coach").prefetch_related("drills")
        qs = qs.filter(coach=self.request.user)
        return qs


class TrainingSessionCreateView(LoginRequiredMixin, CreateView):
    model = TrainingSession
    fields = (
        "date",
        "drills",
    )

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.coach = self.request.user
        return super().form_valid(form)


class TrainingSessionUpdateView(LoginRequiredMixin, UpdateView):
    model = TrainingSession
    fields = (
        "date",
        "drills",
    )

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.coach = self.request.user
        return super().form_valid(form)


class TrainingSessionDetailView(LoginRequiredMixin, DetailView):
    model = TrainingSession

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["ordered_drills"] = [
            (sd.drill, sd.order) for sd in self.get_object().sessiondrills_set.all()
        ]
        print(context["ordered_drills"])
        return context


training_session_list_view = TrainingSessionListView.as_view()
training_session_create_view = TrainingSessionCreateView.as_view()
training_session_update_view = TrainingSessionUpdateView.as_view()
training_session_detail_view = TrainingSessionDetailView.as_view()
