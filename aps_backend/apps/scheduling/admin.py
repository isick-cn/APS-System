from django.contrib import admin
from .models import WorkCenter


@admin.register(WorkCenter)
class WorkCenterAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "available_hours_per_day", "is_active", "created_at")
    search_fields = ("code", "name")
    list_filter = ("is_active",)
