from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from ..filters import SearchFlightFilter
from ..models import Flight
from ..pagination import StandardResultsSetPagination
from ..serializers.search_serializer import SearchFlightOutputSerializer


class SearchList(generics.ListAPIView):
    serializer_class = SearchFlightOutputSerializer
    pagination_class = StandardResultsSetPagination
    filterset_class = SearchFlightFilter

    filter_backends = [DjangoFilterBackend]

    queryset = Flight.objects.all()
    search_fields = ['date_of_departure', 'route__start_point__id', 'route__end_point__id', 'number_of_passengers']

