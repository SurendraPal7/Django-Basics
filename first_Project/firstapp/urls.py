from django.urls import path, re_path
from firstapp import views

urlpatterns = [
    path("",views.hello),
    path("check", views.findEvenOdd),
    
    path("getData/<int:id>/", views.getData),
    path("j",views.getJsonData),
    # what will be the api path for this on the browser? suggest  me 
    
    
    path("jsonData/<str:data>/", views.jsonData),
    path("add/<int:a>/<int:b>/", views.addtion),
    path("greet/<str:name>/",views.greet),
    path("site/<int:id>/", views.siteData),
    path("site/<c>/", views.getData),  #it will take any string/number as input and return the data 
    re_path(r'^user/(?P<username>[a-zA-Z0-9_#@]+)/$', views.userName),  # Example for regex pa
    
re_path(r'^report/(?P<date>\d{4}-\d{2}-\d{2})/$', views.report),  # Example for regex path    
# ramanpal7228@gmail.com
re_path(r'^email/(?P<email>[a-z0-9.]+@[a-z]+\.[a-z]{2,})/$', views.getEmail),  # Example for regex path
   
]