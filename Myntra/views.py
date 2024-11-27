from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def Clothes(request):
    return HttpResponse('<h1>Clothes are available</h1>')

def Gadgets(reuqest):
    return HttpResponse('<h1>All Gadgets are available</h1>')