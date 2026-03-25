from rest_framework import viewsets
from rest_framework.response import Response
from .models import Material, BOM
from .serializers import MaterialSerializer, BOMSerializer


class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all().order_by("-id")
    serializer_class = MaterialSerializer


class BOMViewSet(viewsets.ModelViewSet):
    queryset = BOM.objects.all().order_by("tree_id", "lft")
    serializer_class = BOMSerializer

    def list(self, request, *args, **kwargs):
        roots = BOM.objects.filter(parent__isnull=True).order_by("tree_id", "lft")
        serializer = self.get_serializer(roots, many=True)
        return Response(serializer.data)
