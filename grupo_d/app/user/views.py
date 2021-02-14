from rest_framework.generics import GenericAPIView

from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from app.user.serializers import RegistrationSerializer


class RegistrationView(GenericAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request):
        """
        Create a new user
        """
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "Successfully registered a new user"
            data['email'] = account.email
            data['username'] = account.username
            data['token'] = Token.objects.get(user=account).key
        else:
            data = serializer.errors
        return Response(data)
