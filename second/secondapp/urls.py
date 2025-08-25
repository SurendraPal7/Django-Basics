from django.urls import path, re_path
from secondapp import views
urlpatterns = [
    path("o",views.index),
    # path("h",views.hello),
]
