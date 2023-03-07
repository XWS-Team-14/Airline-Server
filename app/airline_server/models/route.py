import uuid

from django.db import models
from .place import Place


class Route(models.Model):
    """Routes defined for flights

    Attributes:
        id (UUID): Auto generated uuid used to uniquely indentify object
        start_point (Place): Starting point of a Route
        end_point (Place): Ending point of a Route
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    start_point = models.ForeignKey(Place, on_delete=models.CASCADE, null=False, blank=False,
                                    related_name='routes_start_points')
    end_point = models.ForeignKey(Place, on_delete=models.CASCADE, null=False, blank=False,
                                  related_name='routes_end_points')
