from django.urls import path, re_path
from secondapp import views
urlpatterns = [
    path("o",views.index),
    # path("h",views.hello),
    path("table",views.index1),
    path("fruits",views.fruit_list),
    path("resume",views.resume),
    path("filters/",views.filters),
    path("hel/",views.hel),
   path('abo/',views.about, name='about'),
   path('hom', views.home, name='home'),
   path('inde',views.index),
   path('gall',views.gallery),
   path('contact',views.contact, name='contact'),
   re_path(r'^password$', views.password, name='password'),
]
