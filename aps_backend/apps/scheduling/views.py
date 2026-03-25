from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import WorkCenter
from .serializers import WorkCenterSerializer
from .scheduler import heuristic_schedule
from apps.orders.models import WorkOrder


class WorkCenterViewSet(viewsets.ModelViewSet):
    queryset = WorkCenter.objects.all().order_by("-id")
    serializer_class = WorkCenterSerializer


class ScheduleAPIView(APIView):
    def post(self, request):
        work_orders = WorkOrder.objects.select_related("order", "material").filter(status="pending")
        if not work_orders.exists():
            return Response({"detail": "没有待排程工单"}, status=status.HTTP_400_BAD_REQUEST)

        work_centers = WorkCenter.objects.filter(is_active=True)
        if not work_centers.exists():
            return Response({"detail": "没有可用工作中心"}, status=status.HTTP_400_BAD_REQUEST)

        result = heuristic_schedule(list(work_orders), list(work_centers))
        return Response(result, status=status.HTTP_200_OK)
