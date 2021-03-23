from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView

from .models import Drill


class DrillListView(LoginRequiredMixin, ListView):
    model = Drill
    allow_empty = True


class DrillDetailView(LoginRequiredMixin, DetailView):
    model = Drill


class DrillCreateView(LoginRequiredMixin, CreateView):
    model = Drill
    fields = ("name", "description", "image", "duration")


class DrillUpdateView(LoginRequiredMixin, UpdateView):
    model = Drill
    fields = ("name", "description", "image", "duration")


drill_list_view = DrillListView.as_view()
drill_detail_view = DrillDetailView.as_view()
drill_create_view = DrillCreateView.as_view()
drill_update_view = DrillUpdateView.as_view()
