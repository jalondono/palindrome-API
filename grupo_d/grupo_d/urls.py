"""grupo_d URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt import views as jwt_views

from app.palindrome.views import PalindromeView
from app.user.views import RegistrationView


schema_view = get_swagger_view(title='Palindrime Swagger')

admin.site.site_title = 'PRGX'
admin.site.site_header = 'PRGX'

urlpatterns = [
    # url(r'^$', include('rest_framework_swagger.urls')),
    path('admin/', admin.site.urls),
    path('', schema_view, name='docs'),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('palindromo/', PalindromeView.as_view(), name="palindro"),
]
