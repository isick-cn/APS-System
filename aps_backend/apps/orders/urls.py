from rest_framework.routers import DefaultRouter
from .views import ProductionOrderViewSet, WorkOrderViewSet


router = DefaultRouter()
router.register("orders", ProductionOrderViewSet, basename="orders")
router.register("workorders", WorkOrderViewSet, basename="workorders")

urlpatterns = router.urls
