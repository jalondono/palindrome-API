from rest_framework import status
from rest_framework.generics import GenericAPIView
# from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import PalindromeSerializer
from .utils import longest_palindromic


class PalindromeView(GenericAPIView):
    serializer_class = PalindromeSerializer
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        """
        Get the larger palindrome of a substring
        """
        serializer = PalindromeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        text = serializer.validated_data["text"]
        palindromo = longest_palindromic(text)
        return Response({'palindromo': palindromo}, status=status.HTTP_200_OK)
