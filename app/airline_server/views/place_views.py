from rest_framework import generics
from ..models import Place
from ..serializers import PlaceSerializer


class PlaceCreateView(generics.CreateAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


class PlaceListView(generics.ListAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


class PlaceDetailView(generics.RetrieveAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    lookup_field = 'id'  # Or 'slug' if you have a slug field


class PlaceDeleteView(generics.DestroyAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    lookup_field = 'id'


class PlaceUpdateView(generics.UpdateAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    lookup_field = 'id'
