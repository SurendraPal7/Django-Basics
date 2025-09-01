from django.shortcuts import render
from django.http import HttpResponse

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