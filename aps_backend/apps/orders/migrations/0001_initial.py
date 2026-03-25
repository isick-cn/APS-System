from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProductionOrder",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("order_no", models.CharField(max_length=50, unique=True, verbose_name="订单号")),
                ("quantity", models.DecimalField(decimal_places=2, max_digits=10, verbose_name="数量")),
                ("order_date", models.DateField(verbose_name="订单日期")),
                ("due_date", models.DateField(verbose_name="交货日期")),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("draft", "草稿"),
                            ("confirmed", "已确认"),
                            ("processing", "生产中"),
                            ("completed", "已完成"),
                            ("cancelled", "已取消"),
                        ],
                        default="draft",
                        max_length=20,
                        verbose_name="状态",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "product",
                    models.ForeignKey(
                        limit_choices_to={"type": "finished"}, on_delete=django.db.models.deletion.CASCADE, to="products.material"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="WorkOrder",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("quantity", models.DecimalField(decimal_places=2, max_digits=10, verbose_name="数量")),
                ("level", models.IntegerField(default=0, verbose_name="BOM层级")),
                (
                    "status",
                    models.CharField(
                        choices=[("pending", "待排程"), ("scheduled", "已排程"), ("processing", "生产中"), ("completed", "已完成")],
                        default="pending",
                        max_length=20,
                        verbose_name="状态",
                    ),
                ),
                ("start_time", models.DateTimeField(blank=True, null=True, verbose_name="计划开始时间")),
                ("end_time", models.DateTimeField(blank=True, null=True, verbose_name="计划结束时间")),
                ("is_raw_material", models.BooleanField(default=False, verbose_name="是否原材料")),
                ("assigned_work_center", models.CharField(blank=True, max_length=50, null=True, verbose_name="分配的工作中心")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("material", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="products.material")),
                (
                    "order",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="work_orders", to="orders.productionorder"),
                ),
                (
                    "parent",
                    models.ForeignKey(
                        blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name="children", to="orders.workorder"
                    ),
                ),
            ],
            options={"ordering": ["order_id", "level", "id"]},
        ),
    ]
