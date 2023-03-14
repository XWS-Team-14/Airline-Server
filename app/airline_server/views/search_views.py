from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from ..filters import SearchFlightFilter
from ..models import Flight
from ..serializers.search_serializer import SearchFlightOutputSerializer


class SearchList(generics.ListAPIView):
    serializer_class = SearchFlightOutputSerializer
    queryset = Flight.objects.all()
    serializer_class = SearchFlightOutputSerializer
    filter_backends = [DjangoFilterBackend]
    search_fields = ['date_of_departure', 'route__start_point__id', 'route__end_point__id', 'number_of_passengers']
    filterset_class = SearchFlightFilter
