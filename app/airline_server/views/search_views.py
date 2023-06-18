from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from ..filters import SearchFlightFilter, SearchFlightFilterShorter
from ..models import Flight
from ..pagination import StandardResultsSetPagination
from ..serializers.search_serializer import SearchFlightOutputSerializer


class SearchList(generics.ListAPIView):
    serializer_class = SearchFlightOutputSerializer
    pagination_class = StandardResultsSetPagination
    filterset_class = SearchFlightFilter

    filter_backends = [DjangoFilterBackend]

    queryset = Flight.objects.all()

    def get_serializer_context(self):
        # add the query parameter to the serializer context
        context = super().get_serializer_context()
        context['space_needed'] = self.request.query_params.get('space_needed')
        return context


class SearchListSecond(generics.ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = SearchFlightOutputSerializer
    filterset_class = SearchFlightFilterShorter

    filter_backends = [DjangoFilterBackend]

    def get_serializer_context(self):
        # add the query parameter to the serializer context
        context = super().get_serializer_context()
        context['space_needed'] = self.request.query_params.get('space_needed')
        return context
