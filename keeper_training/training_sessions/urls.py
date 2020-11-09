from django.urls import path

from .views import training_session_create_view
from .views import training_session_detail_view
from .views import training_session_list_view
from .views import training_session_update_view

app_name = "training_sessions"
urlpatterns = [
    path("", training_session_list_view, name="list"),
    path("add", training_session_create_view, name="add"),
    path("<int:pk>/", training_session_detail_view, name="detail"),
    path("<int:pk>/update", training_session_update_view, name="update"),
]
