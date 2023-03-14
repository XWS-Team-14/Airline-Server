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
                  'number_of_passengers', 'collective_price', 'status']
        read_only_fields = ['id', 'collective_price', 'status']

    def get_collective_price(self, obj):
        return obj.ticket_price * obj.number_of_passengers

    def get_status(self, obj):
        return obj.get_status()



