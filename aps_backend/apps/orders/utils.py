def explode_bom(order):
    """
    根据订单展开 BOM，生成所有层级的工单

    输入：ProductionOrder 实例
    输出：WorkOrder 列表
    """
    from .models import WorkOrder
    from apps.products.models import BOM

    work_orders = []

    def _explode(material, quantity, level, parent_wo=None):
        wo = WorkOrder.objects.create(
            order=order,
            material=material,
            quantity=quantity,
            level=level,
            parent=parent_wo,
            status="pending",
        )
        work_orders.append(wo)

        bom_items = BOM.objects.filter(material=material)
        if bom_items.exists():
            for item in bom_items:
                child_qty = float(quantity) * float(item.quantity)
                _explode(item.child_material, child_qty, level + 1, wo)
        else:
            wo.is_raw_material = True
            wo.save(update_fields=["is_raw_material"])

        return wo

    _explode(order.product, float(order.quantity), level=0)
    return work_orders
