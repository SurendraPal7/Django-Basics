from django.urls import path
from firstapp import views

urlpatterns = [
    path("home", views.hello),
]