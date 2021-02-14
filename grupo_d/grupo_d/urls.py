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
from django.conf import settings
from django.conf.urls.static import static
# from .router import router
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

from app.palindrome.views import PalindromeView

schema_view = get_swagger_view(title='Palindrime Swagger')

admin.site.site_title = 'PRGX'
admin.site.site_header = 'PRGX'

urlpatterns = [
    # url(r'^$', include('rest_framework_swagger.urls')),
    path('', schema_view),
    # path('register'),
    # path('login'),
    path('admin/', admin.site.urls),
    path('palindromo/', PalindromeView.as_view(), name="palindro"),
]
