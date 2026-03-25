from django.contrib import admin
from .models import ProductionOrder, WorkOrder


@admin.register(ProductionOrder)
class ProductionOrderAdmin(admin.ModelAdmin):
    list_display = ("order_no", "product", "quantity", "order_date", "due_date", "status")
    search_fields = ("order_no",)
    list_filter = ("status",)


@admin.register(WorkOrder)
class WorkOrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "order",
        "material",
        "quantity",
        "level",
        "status",
        "assigned_work_center",
        "start_time",
        "end_time",
    )
    list_filter = ("status", "assigned_work_center", "is_raw_material")
