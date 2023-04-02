from rest_framework import serializers

from ..models import Route


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ['id', 'start_point', 'end_point']
        read_only_fields = ['id']

