from . import views
from django.urls import path 

urlpatterns = [
    path("",views.simple_text,name="simple_text"),
    path("simple_render",views.simple_render,name="simple_render"),
    path("simple_redirect",views.simple_redirect,name="simple_redirect")
]
