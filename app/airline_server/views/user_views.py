from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from airline_server.models import User
from airline_server.serializers.user_serializer import UserSerializer
from datetime import datetime
import uuid
from django.db import transaction


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'email'


class UserDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'


class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'


class CreateApiKeyView(APIView):
    # permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        user_email = request.data.get('user_email')
        valid_due = None if request.data.get('valid_due') == 'forever' else datetime.strptime(request.data.get('valid_due'),
                                                                                         "%Y-%m-%d")

        with transaction.atomic():
            try:
                user = User.objects.select_for_update().get(email=user_email)
            except User.DoesNotExist:
                return Response({"Error": 'No user with this email exists'}, status=status.HTTP_404_NOT_FOUND)

            api_key = str(uuid.uuid4()).replace('-', '')
            user.api_key = api_key
            user.valid_due = valid_due
            user.save()
        if user.valid_due is not None:
            return Response({"APIkey": user.api_key, 'Validity': user.valid_due.strftime("%-d %B, %Y")}, status=status.HTTP_200_OK)
        else:
            return Response({"APIkey": user.api_key, 'Validity': 'Indefinite'}, status=status.HTTP_200_OK)

class GetApiKeyView(APIView):
    def post(self, request, format=None):
        user_email = request.data
        try:
            user = User.objects.get(email=user_email)
        except User.DoesNotExist:
            return Response({"Error": 'No user with this email exists'}, status=status.HTTP_404_NOT_FOUND)
        if user.valid_due is not None:
            return Response({"APIkey": user.api_key, 'Validity': user.valid_due.strftime("%-d %B, %Y")}, status=status.HTTP_200_OK)
        else:
            return Response({"APIkey": user.api_key, 'Validity': 'Indefinite'}, status=status.HTTP_200_OK)