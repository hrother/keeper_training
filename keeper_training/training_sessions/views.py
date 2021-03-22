import json
from typing import Any
from typing import Dict
from typing import Optional
from typing import Type

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import models
from django.db.models.query import QuerySet
from django.forms.forms import BaseForm
from django.forms.models import BaseModelForm
from django.http.response import HttpResponse
from django.http.response import HttpResponseServerError
from django.http.response import JsonResponse
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView
from django.views.generic.base import View

from .models import SessionDrills
from .models import TrainingSession
from keeper_training.drills.models import Drill
from keeper_training.training_sessions.forms import TrainingSessionForm


class TrainingSessionListView(LoginRequiredMixin, ListView):
    model = TrainingSession
    allow_empty = True

    def get_queryset(self) -> QuerySet:
        qs = (
            super()
            .get_queryset()
            .select_related("coach")
            .prefetch_related("sessiondrills_set__drill")
        )
        qs = qs.filter(coach=self.request.user)
        return qs


class TrainingSessionCreateView(LoginRequiredMixin, CreateView):
    model = TrainingSession
    form_class = TrainingSessionForm

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        ctx["action"] = "Create"
        ctx["all_drills"] = Drill.objects.all()
        return ctx

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.coach = self.request.user
        return super().form_valid(form)


class TrainingSessionUpdateView(LoginRequiredMixin, UpdateView):
    model = TrainingSession
    form_class = TrainingSessionForm

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        ctx["action"] = "Update"
        ctx["ordered_drills"] = [
            sd.drill for sd in ctx["object"].sessiondrills_set.all()
        ]
        ctx["all_drills"] = Drill.objects.exclude(
            pk__in=[d.pk for d in ctx["ordered_drills"]]
        )
        return ctx

    def get_form(self, form_class: Optional[Type[BaseForm]] = None) -> BaseForm:
        form = super().get_form(form_class=form_class)
        print(form.is_valid())
        # form.fields["drills"].widget = HiddenInput()
        return form

    def get_form_kwargs(self):
        """Return the keyword arguments for instantiating the form."""
        kwargs = super().get_form_kwargs()
        print("--- form kwargs ---")
        print(kwargs)
        print("--- ---")
        return kwargs

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.coach = self.request.user
        return super().form_valid(form)


class TrainingSessionDetailView(LoginRequiredMixin, DetailView):
    model = TrainingSession

    def get_queryset(self) -> models.query.QuerySet:
        return super().get_queryset().prefetch_related("sessiondrills_set__drill")

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["ordered_drills"] = [
            sd.drill for sd in context["object"].sessiondrills_set.all()
        ]
        return context


class TrainingSessionReorderView(LoginRequiredMixin, View):
    def post(self, request, pk):
        if request.method == "POST" and request.is_ajax():
            try:
                drills = json.loads(request.body)
            except json.JSONDecodeError as e:
                return HttpResponseServerError(str(e))

            for idx, drill_pk in enumerate(drills, start=1):
                sd = SessionDrills.objects.get(drill=drill_pk, session=pk)
                sd.order = idx
                sd.save()
            return JsonResponse({"success": True}, status=200)
        else:
            return JsonResponse({"success": False}, status=400)


training_session_list_view = TrainingSessionListView.as_view()
training_session_create_view = TrainingSessionCreateView.as_view()
training_session_update_view = TrainingSessionUpdateView.as_view()
training_session_detail_view = TrainingSessionDetailView.as_view()
training_session_reorder_view = TrainingSessionReorderView.as_view()
