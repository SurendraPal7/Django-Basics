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

# getting data from external API
def getData(request, id):
    url = f"https://jsonplaceholder.typicode.com/posts/{id}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return JsonResponse(data)
    else:
        return JsonResponse({"error": "Data not found"}, status=404)
    

def getJsonData(request):
    data = {"name": "john","course": "django"}
    return JsonResponse(data)

def jsonData(request,data):
    d={
        "name":"cathy",
        "course":["Django","Python","PHP","Laravel"],
        "city":"Delhi",
    }
    
    if data in d:
        return JsonResponse({data:d[data]})
    else:
        return JsonResponse({"error": "Data not found"}, status=404)
        
     
        
        
def addtion(request,a,b):
    return HttpResponse(f"addition of a and b is :{a+b}")

def greet(request,name):
    return HttpResponse(f"Hello {name}")

def siteData(requet,id):
    return HttpResponse(f"site data is {id}")


def getData(request,c):
    return HttpResponse(f"site data is {c}")