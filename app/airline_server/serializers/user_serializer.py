from ..serializers.ticket_serializer import TicketReducedSerialiser
from rest_framework import serializers
from ..models import User


class UserSerializer(serializers.ModelSerializer):
    tickets = TicketReducedSerialiser(many=True);
    class Meta:
        model = User
        depth = 3
        fields = ['first_name', 'last_name', 'email', 'date_joined', 'last_login', 'is_active', 'tickets']
        read_only_fields = ['id', 'date_joined', 'last_login', 'is_active','tickets']
