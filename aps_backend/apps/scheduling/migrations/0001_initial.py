from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="WorkCenter",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("code", models.CharField(max_length=50, unique=True, verbose_name="编码")),
                ("name", models.CharField(max_length=100, verbose_name="名称")),
                ("available_hours_per_day", models.DecimalField(decimal_places=2, default=8.0, max_digits=5, verbose_name="每日可用工时")),
                ("is_active", models.BooleanField(default=True, verbose_name="是否启用")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
