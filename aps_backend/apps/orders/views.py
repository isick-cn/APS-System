from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import ProductionOrder, WorkOrder
from .serializers import ProductionOrderSerializer, WorkOrderSerializer
from .utils import explode_bom


class ProductionOrderViewSet(viewsets.ModelViewSet):
    queryset = ProductionOrder.objects.all().order_by("-id")
    serializer_class = ProductionOrderSerializer

    @action(detail=True, methods=["post"])
    def generate_workorders(self, request, pk=None):
        order = self.get_object()
        order.work_orders.all().delete()
        work_orders = explode_bom(order)
        serializer = WorkOrderSerializer(work_orders, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class WorkOrderViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = WorkOrder.objects.select_related("order", "material", "parent").all()
    serializer_class = WorkOrderSerializer

    def list(self, request, *args, **kwargs):
        roots = WorkOrder.objects.filter(parent__isnull=True).select_related("order", "material").order_by("order_id", "id")
        serializer = self.get_serializer(roots, many=True)
        return Response(serializer.data)
