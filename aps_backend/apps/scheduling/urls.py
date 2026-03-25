from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import WorkCenterViewSet, ScheduleAPIView


router = DefaultRouter()
router.register("workcenters", WorkCenterViewSet, basename="workcenters")

urlpatterns = [
    path("schedule/", ScheduleAPIView.as_view(), name="schedule"),
] + router.urls
