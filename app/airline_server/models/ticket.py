import uuid

from django.db import models

from .flight import Flight
from .user import User


class Ticket(models.Model):
    """Ticket that user have bought for a flight

    Attributes:
        id (UUID): Auto generated uuid used to uniquely indentify object
        user (User): User that owns the ticket
        flight (Flight): Flight for which ticket is bound
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, related_name='tickets')
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, null=False, blank=False, related_name='tickets')


