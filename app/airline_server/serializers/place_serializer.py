from rest_framework import serializers
from ..models import Place


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ['country', 'airport_city', 'airport_name']
        read_only_fields = ['id']
