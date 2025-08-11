from django.urls import path
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
        path("site/<c>/", views.getData),

    
    
   
]