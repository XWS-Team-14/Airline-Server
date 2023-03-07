import uuid

from django.db import models


class Place(models.Model):
    """Location or place where flights go or takeoff from

    Attributes:
        id (UUID): Auto generated uuid used to uniquely indentify object
        name (str): Name of the place
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
