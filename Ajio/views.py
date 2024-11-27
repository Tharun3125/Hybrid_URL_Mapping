from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse

def Clothes1(request):
    return HttpResponse('<h1>In Ajio Branded Clothes are available</h1>')


def Gadgets1(reuqest):
    return HttpResponse('<h1>In Ajio Gadjets are also available</h1>')