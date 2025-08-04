from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def hello(request):
    return HttpResponse("Hello world!")
     
     
def findEvenOdd(request):
    a=10
    if(a%2==0):
        return HttpResponse("Even Number")
    else:
        return HttpResponse("odd number")
