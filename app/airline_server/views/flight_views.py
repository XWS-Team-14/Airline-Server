from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from ..models import Flight
from ..pagination import StandardResultsSetPagination
from ..serializers import FlightDisplaySerializer, AddFlightSerializer


class FlightList(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = FlightDisplaySerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    queryset = Flight.objects.all()


class FlightCreateView(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Flight.objects.all()
    serializer_class = AddFlightSerializer


class FlightDeleteView(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Flight.objects.all()
    serializer_class = FlightDisplaySerializer
    lookup_field = 'id'

    def destroy(self, *args, **kwargs):
        serializer = self.get_serializer(self.all())
        super().destroy(*args, **kwargs)
        return Response(serializer.data)


class FlightUpdateView(generics.UpdateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Flight.objects.all()
    serializer_class = FlightDisplaySerializer
    lookup_field = 'id'
