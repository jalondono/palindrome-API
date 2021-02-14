from rest_framework.generics import GenericAPIView

from rest_framework.response import Response

from .serializers import PalindromeSerializer
from .utils import get_palindrome


class PalindromeView(GenericAPIView):
    serializer_class = PalindromeSerializer

    def get(self, request):
        """
        """
        pass

    def post(self, request):
        """
        Get the larger palindrome of a substring
        """
        serializer = PalindromeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        text = serializer.validated_data["text"]
        palindromo = get_palindrome(text)
        return Response({'palindromo': palindromo})
        # else:
        #     raise ValidationError
