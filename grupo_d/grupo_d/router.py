from rest_framework import routers

from app.palindrome.views import PalindromeViewSet
router = routers.DefaultRouter(trailing_slash=True)

router.register(r'', PalindromeViewSet, basename='pali')
