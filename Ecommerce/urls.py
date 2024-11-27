"""
URL configuration for Ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include
from Myntra.views import *
from Ajio.views import *
import FLip
import Amazon

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Clothes/',Clothes,name='Clothes'),
    path('Gadgets/',Gadgets,name='Gadgets'),
    path('Clothes1/',Clothes1,name='Clothes1'),
    path('Gadgets1/',Gadgets1,name='Gadgets1'),
    path('FLip/',include('FLip.urls')),
    path('Amazon/',include('Amazon.urls')),

]
