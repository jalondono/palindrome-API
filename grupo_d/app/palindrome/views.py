from django.http import HttpResponseBadRequest
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .utils import get_palindrome
from rest_framework.exceptions import ValidationError, ParseError


class PalindromeViewSet(viewsets.ModelViewSet):
    def list(self, request, *args, **kwargs):
        """
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        pass

    def create(self, request, *args, **kwargs):
        """
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        text = request.data.get('text')
        if text:
            palindromo = get_palindrome(text)
            return Response({'palindromo': palindromo})
        else:
            raise ValidationError
