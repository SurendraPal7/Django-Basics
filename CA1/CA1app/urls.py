from django.urls import path, re_path

from CA1app import views


urlpatterns = [
    path('home', views.home, name='home'),
    path('ab', views.about, name='ab'),
    path('contact', views.contact, name='contact'),
]
