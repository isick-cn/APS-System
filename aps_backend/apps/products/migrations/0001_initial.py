from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Material",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("code", models.CharField(max_length=50, unique=True, verbose_name="编码")),
                ("name", models.CharField(max_length=200, verbose_name="名称")),
                ("type", models.CharField(choices=[("finished", "成品"), ("semi", "半成品"), ("raw", "原材料")], max_length=20, verbose_name="类型")),
                ("unit", models.CharField(default="个", max_length=10, verbose_name="单位")),
                ("lead_time", models.IntegerField(default=0, verbose_name="提前期(天)")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="ProcessRoute",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("version", models.CharField(default="1.0", max_length=10, verbose_name="版本")),
                ("is_active", models.BooleanField(default=True, verbose_name="是否启用")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "material",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="routes", to="products.material"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProcessStep",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("sequence", models.IntegerField(verbose_name="工序序号")),
                ("name", models.CharField(max_length=100, verbose_name="工序名称")),
                ("work_center", models.CharField(max_length=50, verbose_name="工作中心")),
                ("duration", models.IntegerField(verbose_name="加工时间(分钟)")),
                ("setup_time", models.IntegerField(default=0, verbose_name="准备时间(分钟)")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "route",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="steps", to="products.processroute"),
                ),
            ],
            options={"ordering": ["sequence"]},
        ),
        migrations.CreateModel(
            name="BOM",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("quantity", models.DecimalField(decimal_places=2, max_digits=10, verbose_name="用量")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("lft", models.PositiveIntegerField(editable=False)),
                ("rght", models.PositiveIntegerField(editable=False)),
                ("tree_id", models.PositiveIntegerField(db_index=True, editable=False)),
                ("level", models.PositiveIntegerField(editable=False)),
                (
                    "child_material",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="bom_as_child", to="products.material"),
                ),
                ("material", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="bom_as_parent", to="products.material")),
                (
                    "parent",
                    mptt.fields.TreeForeignKey(
                        blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name="children", to="products.bom"
                    ),
                ),
            ],
            options={"abstract": False},
        ),
    ]
