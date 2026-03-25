from django.db import models
from apps.products.models import Material


class ProductionOrder(models.Model):
    STATUS_CHOICES = [
        ("draft", "草稿"),
        ("confirmed", "已确认"),
        ("processing", "生产中"),
        ("completed", "已完成"),
        ("cancelled", "已取消"),
    ]
    order_no = models.CharField("订单号", max_length=50, unique=True)
    product = models.ForeignKey(Material, on_delete=models.CASCADE, limit_choices_to={"type": "finished"})
    quantity = models.DecimalField("数量", max_digits=10, decimal_places=2)
    order_date = models.DateField("订单日期")
    due_date = models.DateField("交货日期")
    status = models.CharField("状态", max_length=20, choices=STATUS_CHOICES, default="draft")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "生产订单"
        verbose_name_plural = "生产订单"

    def __str__(self):
        return self.order_no


class WorkOrder(models.Model):
    STATUS_CHOICES = [
        ("pending", "待排程"),
        ("scheduled", "已排程"),
        ("processing", "生产中"),
        ("completed", "已完成"),
    ]
    order = models.ForeignKey(ProductionOrder, on_delete=models.CASCADE, related_name="work_orders")
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    quantity = models.DecimalField("数量", max_digits=10, decimal_places=2)
    level = models.IntegerField("BOM层级", default=0)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="children")
    status = models.CharField("状态", max_length=20, choices=STATUS_CHOICES, default="pending")
    start_time = models.DateTimeField("计划开始时间", null=True, blank=True)
    end_time = models.DateTimeField("计划结束时间", null=True, blank=True)
    is_raw_material = models.BooleanField("是否原材料", default=False)
    assigned_work_center = models.CharField("分配的工作中心", max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order_id", "level", "id"]
        verbose_name = "工单"
        verbose_name_plural = "工单"

    def __str__(self):
        return f"{self.order.order_no} - {self.material.name}"
