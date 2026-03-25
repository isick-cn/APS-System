from rest_framework import serializers
from .models import ProductionOrder, WorkOrder


class ProductionOrderSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source="product.name", read_only=True)

    class Meta:
        model = ProductionOrder
        fields = "__all__"


class WorkOrderSerializer(serializers.ModelSerializer):
    material_name = serializers.CharField(source="material.name", read_only=True)
    order_no = serializers.CharField(source="order.order_no", read_only=True)
    children = serializers.SerializerMethodField()

    class Meta:
        model = WorkOrder
        fields = "__all__"

    def get_children(self, obj):
        return WorkOrderSerializer(obj.children.all(), many=True).data
