from django.urls import path
from . import views

urlpatterns = [
    path("",views.list_album,name="list_album"),
    path("delete/<int:pk>/",views.delete_album,name="delete_album"),
    path("update/<int:pk>/",views.update_album,name="update_album"),
    path("add/",views.add_album,name="add_album"),
]
