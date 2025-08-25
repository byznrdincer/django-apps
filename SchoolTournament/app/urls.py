from django.urls import path 
from . import views

urlpatterns = [
    path("",views.add_student,name="add_student"),
    path("delete_student/<int:pk>/",views.delete_student,name="delete_student"),
    path("update_student/<int:pk>/",views.update_student,name="update_student"),
    path("all_student",views.all_student,name="all_student"),
    
    path("",views.add_team,name="add_team"),
    path("delete_team/<int:pk>/",views.delete_team,name="delete_team"),
    path("update_team/<int:pk>/",views.update_team,name="update_team"),
    path("all_team/",views.all_team,name="all_team"),
    
    path("",views.add_match,name="add_match"),
    path("delete_match/<int:pk>/",views.delete_match,name="delete_match"),
    path("update_match/<int:pk>/",views.update_match,name="update_match"),
    path("all_match",views.all_match,name="all_match"),
    
    path("",views.add_team,name="add_team"),
    path("delete_team/<int:pk>/",views.delete_team,name="delete_team"),
    path("update_team/<int:pk>",views.update_team,name="update_team"),
    path("all_team",views.all_team,name="all_team")
]
