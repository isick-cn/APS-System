from datetime import datetime, timedelta
from collections import defaultdict


def heuristic_schedule(work_orders, work_centers):
    """
    启发式排程算法
    规则：按交货期升序 + 同订单按 level 升序 + 设备负载均衡
    """
    orders_dict = {}
    for wo in work_orders:
        if wo.order_id not in orders_dict:
            orders_dict[wo.order_id] = {
                "order": wo.order,
                "due_date": wo.order.due_date,
                "work_orders": [],
            }
        orders_dict[wo.order_id]["work_orders"].append(wo)

    for order_data in orders_dict.values():
        order_data["work_orders"].sort(key=lambda x: x.level)

    sorted_orders = sorted(orders_dict.values(), key=lambda x: x["due_date"])

    work_center_end_time = defaultdict(lambda: datetime.now())
    schedule_results = []

    for order_data in sorted_orders:
        for wo in order_data["work_orders"]:
            best_center = min(work_centers, key=lambda wc: work_center_end_time[wc.code])
            process_time = float(wo.quantity) * 0.5
            start_time = work_center_end_time[best_center.code]
            end_time = start_time + timedelta(hours=process_time)
            work_center_end_time[best_center.code] = end_time

            wo.start_time = start_time
            wo.end_time = end_time
            wo.assigned_work_center = best_center.code
            wo.status = "scheduled"
            wo.save(update_fields=["start_time", "end_time", "assigned_work_center", "status"])

            schedule_results.append(
                {
                    "work_order_id": wo.id,
                    "material_name": wo.material.name,
                    "quantity": wo.quantity,
                    "work_center": best_center.code,
                    "start_time": start_time,
                    "end_time": end_time,
                }
            )

    return schedule_results
