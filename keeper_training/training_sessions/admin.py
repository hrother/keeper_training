from django.contrib import admin

from .models import SessionDrills
from .models import TrainingSession


class SessionDrillsInline(admin.TabularInline):
    model = SessionDrills


@admin.register(TrainingSession)
class TrainingSessionAdmin(admin.ModelAdmin):
    inlines = (SessionDrillsInline,)


# admin.site.register(SessionDrillsInline)
