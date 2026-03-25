from rest_framework import serializers
from .models import Material, BOM, ProcessRoute, ProcessStep


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = "__all__"


class ProcessStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcessStep
        fields = "__all__"


class ProcessRouteSerializer(serializers.ModelSerializer):
    steps = ProcessStepSerializer(many=True, read_only=True)

    class Meta:
        model = ProcessRoute
        fields = "__all__"


class BOMSerializer(serializers.ModelSerializer):
    material_name = serializers.CharField(source="material.name", read_only=True)
    child_material_name = serializers.CharField(source="child_material.name", read_only=True)
    children = serializers.SerializerMethodField()

    class Meta:
        model = BOM
        fields = "__all__"

    def get_children(self, obj):
        return BOMSerializer(obj.get_children(), many=True).data
