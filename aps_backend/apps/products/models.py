from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Material(models.Model):
    TYPE_CHOICES = [
        ("finished", "成品"),
        ("semi", "半成品"),
        ("raw", "原材料"),
    ]
    code = models.CharField("编码", max_length=50, unique=True)
    name = models.CharField("名称", max_length=200)
    type = models.CharField("类型", max_length=20, choices=TYPE_CHOICES)
    unit = models.CharField("单位", max_length=10, default="个")
    lead_time = models.IntegerField("提前期(天)", default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "物料"
        verbose_name_plural = "物料"

    def __str__(self):
        return f"{self.code} - {self.name}"


class BOM(MPTTModel):
    parent = TreeForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="children")
    material = models.ForeignKey(Material, on_delete=models.CASCADE, related_name="bom_as_parent")
    child_material = models.ForeignKey(Material, on_delete=models.CASCADE, related_name="bom_as_child")
    quantity = models.DecimalField("用量", max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class MPTTMeta:
        order_insertion_by = ["id"]

    class Meta:
        verbose_name = "BOM关系"
        verbose_name_plural = "BOM关系"

    def __str__(self):
        return f"{self.material.name} -> {self.child_material.name} x {self.quantity}"


class ProcessRoute(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE, related_name="routes")
    version = models.CharField("版本", max_length=10, default="1.0")
    is_active = models.BooleanField("是否启用", default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "工艺路线"
        verbose_name_plural = "工艺路线"

    def __str__(self):
        return f"{self.material.name} - v{self.version}"


class ProcessStep(models.Model):
    route = models.ForeignKey(ProcessRoute, on_delete=models.CASCADE, related_name="steps")
    sequence = models.IntegerField("工序序号")
    name = models.CharField("工序名称", max_length=100)
    work_center = models.CharField("工作中心", max_length=50)
    duration = models.IntegerField("加工时间(分钟)")
    setup_time = models.IntegerField("准备时间(分钟)", default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["sequence"]
        verbose_name = "工序"
        verbose_name_plural = "工序"

    def __str__(self):
        return f"{self.route.material.name} - {self.sequence}.{self.name}"
