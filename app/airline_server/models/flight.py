import uuid
import datetime

from django.db import models

from .route import Route


class Flight(models.Model):
    """Class used to model flights in the app

    Attributes:
        id (UUID): Auto generated uuid used to uniquely indentify object
        route (Route): Foreign Key linked to Route model
        date_of_departure (date): Date formatted like hh:mm
        ticket_price (float): Float value of a tickets price in euros
        number_of_seats (int): Number of seats - flight tickets available in total
        number_of_free_spaces (int): Number of passengers - flight tickets sold
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    route = models.ForeignKey(Route, on_delete=models.CASCADE, null=False, blank=False)
    date_of_departure = models.DateTimeField(null=False, blank=False)
    ticket_price = models.FloatField(null=False, blank=False)
    number_of_seats = models.IntegerField(null=False, blank=False)
    number_of_free_spaces = models.IntegerField(null=False, blank=False)

    def get_status(self, space_needed):
        """Calculates if it's possible to book the flight

        Takes into the account date and number of spaces left

        """
        return datetime.datetime.now().timestamp() < self.date_of_departure.timestamp() \
            and self.number_of_free_spaces >= space_needed
