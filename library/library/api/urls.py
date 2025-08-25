from django.urls import path
from . import views

urlpatterns = [
    path('',views.add_book,name="add_book"),
    path('delete/<int:pk>/',views.delete_books,name="delete_books"),
    path('all_books/',views.all_books,name="all_books"),
    path('update_books/<int:pk>/',views.update_books,name="update_books")
]
