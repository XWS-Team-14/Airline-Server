from rest_framework import serializers
from ..models import Place


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ['country', 'airport_city', 'airport_name']
        read_only_fields = ['id']

    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Place name should be at least 2 characters long.")
        return value

