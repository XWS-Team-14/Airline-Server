from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from ..models import Flight
from ..models import User
from airline_server.models import Ticket
from airline_server.serializers.ticket_serializer import TicketSerializer
from datetime import datetime


class TicketCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class TicketListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class TicketDetailView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    lookup_field = 'id'


class TicketDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    lookup_field = 'id'


class TicketUpdateView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    lookup_field = 'id'


class TicketPurchaseView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        user_email = request.data.get('user_email')
        flight_id = request.data.get('flight_id')
        num_of_tickets = request.data.get('num_of_tickets')

        with transaction.atomic():
            flight = Flight.objects.select_for_update().get(pk=flight_id)
            if flight.get_status(num_of_tickets) == False:
                return Response({"Fail": "Unable to purchase tickets, flight departed or sold out."},
                                status=status.HTTP_400_BAD_REQUEST)
            user = User.objects.get(email=user_email)
            for i in range(num_of_tickets):
                ticket = Ticket(user=user, flight=flight)
                ticket.save()
            flight.number_of_free_spaces = flight.number_of_free_spaces - num_of_tickets
            flight.save()
        return Response({}, status=status.HTTP_200_OK)


class ApiKeyPurchaseView(APIView):
    def post(self, request):
        api_key = request.META.get('HTTP_API_KEY')
        flight_id = request.data.get('flight_id')
        num_of_tickets = request.data.get('num_of_tickets')
        if api_key is None:
            return Response({"Error": 'Api key header missing'}, status=status.HTTP_401_UNAUTHORIZED)
        with transaction.atomic():
            try:
                user = User.objects.get(api_key=api_key)
            except User.DoesNotExist:
                return Response({"Error": 'Invalid API Key.'}, status=status.HTTP_401_UNAUTHORIZED)
            # valid_due null signals infinite duration
            if user.valid_due is not None and user.valid_due.timestamp() < datetime.now().timestamp():
                return Response({"Error": 'API Key has expired.'}, status=status.HTTP_401_UNAUTHORIZED)

            flight = Flight.objects.select_for_update().get(pk=flight_id)
            if not flight.get_status(num_of_tickets):
                return Response({"Error": "Unable to purchase ticket. The flight has departed or sold out."},
                                status=status.HTTP_400_BAD_REQUEST)
            for i in range(int(num_of_tickets)):
                ticket = Ticket(user=user, flight=flight)
                ticket.save()
            flight.number_of_free_spaces = flight.number_of_free_spaces - int(num_of_tickets)
            flight.save()
        return Response({}, status=status.HTTP_200_OK)
