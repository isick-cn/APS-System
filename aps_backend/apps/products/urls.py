from rest_framework.routers import DefaultRouter
from .views import MaterialViewSet, BOMViewSet


router = DefaultRouter()
router.register("materials", MaterialViewSet, basename="materials")
router.register("bom", BOMViewSet, basename="bom")

urlpatterns = router.urls
