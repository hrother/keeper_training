from django.views.generic import DetailView, ListView

from .models import Drill


class DrillListView(ListView):
    model = Drill
    allow_empty = True


class DrillDetailView(DetailView):
    model = Drill


drill_list_view = DrillListView.as_view()
drill_detail_view = DrillDetailView.as_view()
