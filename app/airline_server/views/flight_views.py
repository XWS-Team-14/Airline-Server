from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from ..models import Flight
from ..pagination import StandardResultsSetPagination
from ..serializers.flight_serializer import FlightDisplaySerializer, AddFlightSerializer


class FlightList(generics.ListAPIView):
    serializer_class = FlightDisplaySerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    queryset = Flight.objects.all()


class FlightCreateView(generics.CreateAPIView):
    queryset = Flight.objects.all()
    serializer_class = AddFlightSerializer


class FlightDeleteView(generics.DestroyAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightDisplaySerializer
    lookup_field = 'id'


class FlightUpdateView(generics.UpdateAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightDisplaySerializer
    lookup_field = 'id'
