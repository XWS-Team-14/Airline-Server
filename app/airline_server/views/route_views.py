from rest_framework import generics

from ..models import Route
from ..serializers import RouteSerializer
from ..serializers.search_serializer import RouteOutputSerializer


class RouteCreateView(generics.CreateAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer


class RouteListView(generics.ListAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer


class RouteDetailView(generics.RetrieveAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    lookup_field = 'id'  # Or 'slug' if you have a slug field


class RouteDeleteView(generics.DestroyAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    lookup_field = 'id'


class RouteUpdateView(generics.UpdateAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    lookup_field = 'id'


class RouteListViewWithPlaces(generics.ListAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteOutputSerializer