from django.urls import path

from .views import drill_create_view
from .views import drill_detail_view
from .views import drill_list_view
from .views import drill_update_view

app_name = "drills"
urlpatterns = [
    path("", drill_list_view, name="list"),
    path("<slug:slug>/", drill_detail_view, name="detail"),
    path("add", drill_create_view, name="add"),
    path("<slug:slug>/update", drill_update_view, name="update"),
]
