from django.urls import path
from firstapp import views

urlpatterns = [
    path("home", views.hello),
    path("check", views.findEvenOdd),
    
    path("getData/<int:id>/", views.getData),
    
]