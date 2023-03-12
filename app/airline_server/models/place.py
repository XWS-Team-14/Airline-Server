import uuid

from django.db import models


class Place(models.Model):
    """Location or place where flights go or takeoff from

    Attributes:
        id (UUID): Auto generated uuid used to uniquely indentify object
        country (str): Name of the country where the place is located
        airport_city (str): City where airport is located at
        airport_name (str): Name of the airport
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    country = models.CharField(max_length=100, null=False, blank=False)
    airport_city = models.CharField(max_length=100, null=False, blank=False)
    airport_name = models.CharField(max_length=100, null=False, blank=False)
