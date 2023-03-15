from rest_framework import serializers

from .place_serializer import PlaceSerializer
from ..models import Flight, Route


class RouteOutputSerializer(serializers.ModelSerializer):
    start_point = PlaceSerializer()
    end_point = PlaceSerializer()

    class Meta:
        model = Route
        fields = ['id', 'start_point', 'end_point']
        read_only_fields = ['id']


class SearchFlightOutputSerializer(serializers.ModelSerializer):
    route = RouteOutputSerializer()
    collective_price = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()

    class Meta:
        model = Flight
        fields = ['id', 'route', 'date_of_departure', 'ticket_price', 'number_of_seats',
                  'number_of_free_spaces', 'collective_price', 'status']
        read_only_fields = ['id', 'collective_price', 'status']

    def get_collective_price(self, obj):
        """Calculates collective price for wanted tickets (or return 0 if there's error)"""
        value = self.context.get('space_needed')
        if value is not None and bool(value):
            return obj.ticket_price * int(value)
        else:
            return 0

    def get_status(self, obj):
        return obj.get_status()



