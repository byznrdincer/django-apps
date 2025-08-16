from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('goreviki/',views.goreviki,name="goreviki"),
    path('gorevuc/',views.gorevuc,name="gorevuc")
    
]

