from django.http import HttpResponse
from django.shortcuts import render
import requests
from django.http import JsonResponse

# Create your views here.


def hello(request):
    return HttpResponse("Hello world!")
                                                     
     
def findEvenOdd(request):
    a=10
    if(a%2==0):
        return HttpResponse("Even Number")
    else:
        return HttpResponse("odd number")


def getData(request, id):
    url = f"https://jsonplaceholder.typicode.com/posts/{id}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return JsonResponse(data)
    else:
        return JsonResponse({"error": "Data not found"}, status=404)