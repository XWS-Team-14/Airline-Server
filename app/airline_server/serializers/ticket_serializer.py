from rest_framework import serializers
from ..models import Ticket

class TicketSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Ticket
        fields = ['id', 'user', 'flight']
        read_only_fields = ['id']
        
class TicketReducedSerialiser(serializers.ModelSerializer):
    class Meta: 
        model = Ticket
        depth = 3
        fields = ['id', 'flight']
