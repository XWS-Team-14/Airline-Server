from rest_framework import serializers
from .route_serializer import RouteSerializer
from .search_serializer import RouteOutputSerializer
from ..models import Flight, Route


class FlightDisplaySerializer(serializers.ModelSerializer):
    route = RouteOutputSerializer()
    class Meta:
        model = Flight
        fields = ['id', 'route', 'date_of_departure', 'ticket_price', 'number_of_seats', 'number_of_free_spaces']
        read_only_fields = ['id']

class AddFlightSerializer(serializers.ModelSerializer):
    route = RouteSerializer
    class Meta:
        model = Flight
        fields = ['id', 'route', 'date_of_departure', 'ticket_price', 'number_of_seats', 'number_of_free_spaces']
        read_only_fields = ['id']


