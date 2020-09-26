from django.urls import path

from .views import drill_detail_view, drill_list_view

app_name = "drills"
urlpatterns = [
    path("", drill_list_view, name="list"),
    path("<slug:slug>/", drill_detail_view, name="detail"),
]
