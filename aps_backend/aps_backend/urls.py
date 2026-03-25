from django.contrib import admin
from django.urls import include, path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="APS 生产排程系统 API",
        default_version="v1",
        description="APS 生产排程系统 API 文档",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

admin.site.site_header = "APS 生产排程系统"
admin.site.site_title = "APS 管理后台"
admin.site.index_title = "后台管理"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("apps.products.urls")),
    path("api/", include("apps.orders.urls")),
    path("api/", include("apps.scheduling.urls")),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
