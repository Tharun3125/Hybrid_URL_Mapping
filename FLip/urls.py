from django.urls import path
from FLip.views import *

urlpatterns = [
    path('Clothes2/',Clothes2,name='Clothes2'),
    path('Gadgets2/',Gadgets2,name='Gadgets2'),
]