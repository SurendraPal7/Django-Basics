from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here..
def index(request):
    return render(request,'myapp/index.html')
def index1(request):
    return render(request,'myapp/index2.html')

def fruit_list(request):
    fruits = ['Apple', 'Banana', 'Orange', 'Mango']
    return render(request, 'myapp/fruits.html', {'fruits': fruits})

def resume(request):
    return render(request,'myapp/index3.html')


def filters(request):
    context={
        "name":'john wick',
        "date":"2024-06-15"
        # "date":datetime.now()
        
    }
    return render(request,'myapp/filter.html',context)

def hel(request):
    context={
        "message":"Django",
        "marks":65
    }
    return render(request,'myapp/hello.html',context)