from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from .models import Material, BOM, ProcessRoute, ProcessStep


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "type", "unit", "lead_time", "created_at")
    search_fields = ("code", "name")
    list_filter = ("type",)


@admin.register(BOM)
class BOMAdmin(DraggableMPTTAdmin):
    list_display = ("tree_actions", "indented_title", "material", "child_material", "quantity")
    list_display_links = ("indented_title",)


class ProcessStepInline(admin.TabularInline):
    model = ProcessStep
    extra = 1


@admin.register(ProcessRoute)
class ProcessRouteAdmin(admin.ModelAdmin):
    list_display = ("material", "version", "is_active", "created_at")
    list_filter = ("is_active",)
    inlines = [ProcessStepInline]
