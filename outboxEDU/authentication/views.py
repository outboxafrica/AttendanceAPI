from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from .models import User
from .serializer import RegistrationSerializer


class RegistrationAPIView(APIView):
    "View to Create a user"
    permission_classes = (AllowAny, )
    serializer_class = RegistrationSerializer

    def post(self, request, format=None):

        user = self.request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_data = serializer.data

        # response_data = {
        #     "username": user['usename'],
        #     "email": user['email'],
        #     "message": "you have succesfully  registered"
        # }

        return Response(user_data, status=status.HTTP_201_CREATED)
