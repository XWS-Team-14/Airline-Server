from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from ..models import Flight
from ..models import User
from ..models import Ticket
from airline_server.models import Ticket
from airline_server.serializers.ticket_serializer import TicketSerializer

class TicketCreateView(generics.CreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class TicketListView(generics.ListAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class TicketDetailView(generics.RetrieveAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    lookup_field = 'id'


class TicketDeleteView(generics.DestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    lookup_field = 'id'


class TicketUpdateView(generics.UpdateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    lookup_field = 'id'

class TicketPurchaseView(APIView):
    def post(self, request, format=None):
        user_email = request.data.get('user_email')
        flight_id = request.data.get('flight_id')
        num_of_tickets = request.data.get('num_of_tickets')
        
        with transaction.atomic():
            flight = Flight.objects.select_for_update().get(pk=flight_id);
            if flight.get_status(num_of_tickets) == False:
                return Response({"Fail": "Unable to purchase tickets, flight departed or sold out."},status=status.HTTP_400_BAD_REQUEST)
            user = User.objects.get(email = user_email)
            for i in range(num_of_tickets):
                ticket = Ticket(user=user,flight=flight)
                ticket.save();
            flight.number_of_free_spaces = flight.number_of_free_spaces - num_of_tickets;
            flight.save()
        return Response(status=status.HTTP_200_OK)

