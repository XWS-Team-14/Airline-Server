from rest_framework import generics
from rest_framework.permissions import AllowAny

from airline_server.models import User
from airline_server.serializers.register_serializer import RegisterSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer