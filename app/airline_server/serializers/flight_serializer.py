from rest_framework import serializers
from .route_serializer import RouteSerializer
from .search_serializer import RouteOutputSerializer
from ..models import Flight, Route


class FlightSerializer(serializers.ModelSerializer):

    status = serializers.SerializerMethodField()

    class Meta:
        model = Flight
        fields = ['id', 'route', 'date_of_departure', 'ticket_price', 'number_of_seats', 'number_of_free_spaces',
                  'status']
        read_only_fields = ['id',  'status']



    def get_status(self, obj):
        return obj.get_status()
