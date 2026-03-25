from django.db import models


class WorkCenter(models.Model):
    code = models.CharField("编码", max_length=50, unique=True)
    name = models.CharField("名称", max_length=100)
    available_hours_per_day = models.DecimalField("每日可用工时", max_digits=5, decimal_places=2, default=8.0)
    is_active = models.BooleanField("是否启用", default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "工作中心"
        verbose_name_plural = "工作中心"

    def __str__(self):
        return f"{self.code} - {self.name}"
