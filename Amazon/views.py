from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def Clothes2(request):
    return HttpResponse('<h1>Amazon is not good for colthes</h1>')

def Gadgets2(request):
    return HttpResponse('<h1>Amazon is very good for Gadgets</h1>')