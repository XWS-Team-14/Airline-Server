from rest_framework import serializers
from ..models import Route
from .place_serializer import PlaceSerializer


class RouteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Route
        fields = ['start_point', 'end_point']
        read_only_fields = ['id']

