from django.contrib import admin

from .models import SessionDrills
from .models import TrainingSession


class SessionDrillsInline(admin.TabularInline):
    model = SessionDrills


class TrainingSessionAdmin(admin.ModelAdmin):
    inlines = (SessionDrillsInline,)


admin.site.register(TrainingSession, TrainingSessionAdmin)
# admin.site.register(SessionDrillsInline)
