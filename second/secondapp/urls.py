from django.urls import path, re_path
from secondapp import views
urlpatterns = [
    path("o",views.index),
    # path("h",views.hello),
    path("table",views.index1),
    path("fruits",views.fruit_list),
    path("resume",views.resume),
]
