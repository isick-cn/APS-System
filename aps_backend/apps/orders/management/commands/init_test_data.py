from datetime import date, timedelta
from django.core.management.base import BaseCommand
from django.db import transaction
from apps.products.models import Material, BOM
from apps.orders.models import ProductionOrder
from apps.scheduling.models import WorkCenter


class Command(BaseCommand):
    help = "一键初始化 APS 测试数据"

    @transaction.atomic
    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING("开始初始化测试数据..."))

        # 物料
        fg, _ = Material.objects.get_or_create(
            code="FG001",
            defaults={"name": "成品A", "type": "finished", "unit": "件", "lead_time": 2},
        )
        sm, _ = Material.objects.get_or_create(
            code="SM001",
            defaults={"name": "半成品B", "type": "semi", "unit": "件", "lead_time": 1},
        )
        rm1, _ = Material.objects.get_or_create(
            code="RM001",
            defaults={"name": "原料C", "type": "raw", "unit": "kg", "lead_time": 0},
        )
        rm2, _ = Material.objects.get_or_create(
            code="RM002",
            defaults={"name": "原料D", "type": "raw", "unit": "kg", "lead_time": 0},
        )

        # BOM
        node_fg_sm, _ = BOM.objects.get_or_create(material=fg, child_material=sm, defaults={"quantity": 2})
        BOM.objects.get_or_create(parent=node_fg_sm, material=sm, child_material=rm1, defaults={"quantity": 3})
        BOM.objects.get_or_create(parent=node_fg_sm, material=sm, child_material=rm2, defaults={"quantity": 1.5})

        # 工作中心
        WorkCenter.objects.get_or_create(
            code="WC01",
            defaults={"name": "装配线1", "available_hours_per_day": 8, "is_active": True},
        )
        WorkCenter.objects.get_or_create(
            code="WC02",
            defaults={"name": "装配线2", "available_hours_per_day": 8, "is_active": True},
        )

        # 订单
        today = date.today()
        ProductionOrder.objects.get_or_create(
            order_no=f"PO{today.strftime('%Y%m%d')}001",
            defaults={
                "product": fg,
                "quantity": 20,
                "order_date": today,
                "due_date": today + timedelta(days=7),
                "status": "confirmed",
            },
        )

        self.stdout.write(self.style.SUCCESS("测试数据初始化完成。"))
        self.stdout.write("可在订单页面点击“生成工单”，然后在排程页面执行排程。")
