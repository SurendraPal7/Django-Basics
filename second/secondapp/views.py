from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import re

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

def about(request):
    return render(request,'myapp/about.html')



def home(request):
    return render(request,'myapp/home.html')

def index(request):
    return render(request,'myapp/index.html')

def gallery(request):
    return render(request, 'myapp/gallery.html')


def contact(request):
    name=None
    email=None
    phone=None
    age=None
    message=None
    
    
    
     
    if request.method=="POST":
        
        
        name=request.POST.get("name")
        
        email=request.POST.get("email")
        age=request.POST.get("age")
        message=request.POST.get("message")
    elif request.method=="GET":
        name=request.GET.get("name")
        email=request.GET.get("email")
        age=request.GET.get("age")
        message=request.GET.get("message")
    return render(request,'myapp/contact.html',{"name":name,"email":email,"age":age,"message":message})

   
def password(request):
    message = ''
    if request.method == 'POST':
        password= request.POST.get('password')
        # regex for password validation
       
        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
        if re.match(pattern, password):
            message = 'Password is valid.'
        else:
            message = 'Password is invalid. It must be at least 8 characters long and include at least one uppercase letter, one lowercase letter, one digit, and one special character.'
    return render(request, 'myapp/password.html', {'message': message})
