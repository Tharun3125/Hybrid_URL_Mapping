from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def Clothes2(request):
    return HttpResponse('<h1>In Flip clothes are not available</h1>')

def Gadgets2(request):
    return HttpResponse('<h1>In FLip gadgets are main products</h1>')