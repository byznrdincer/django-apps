from django.urls import path 
from . import views

urlpatterns = [
    path('',views.add_student,name="add_student"),
    path('all_student/',views.all_student,name="all_student"),
    path('delete_student/<int:pk>/',views.delete_student,name="delete_student"),
    path('update_student/<int:pk>/',views.update_student,name="update_student")
]
