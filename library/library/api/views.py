from django import forms
from django.shortcuts import render,redirect,get_object_or_404
from .models import Book
from .forms import BookForm

def add_book(request):
    if request.method=="POST":
        form=BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("all_books")
    else:
        form=BookForm()
        
    return render(request,"Add_book.html",{"form":form})

def all_books(request):
    books=Book.objects.all()
    return render(request,"all_books.html",{"books":books})
    
def delete_books(request,pk):
    books=get_object_or_404(Book,pk=pk)
    books.delete()
    return redirect("all_books")

def update_books(request,pk):
    books=get_object_or_404(Book,pk=pk)
    if request.method=="POST":
        form=BookForm(request.POST,instance=books)
        if form.is_valid():
            form.save()
            return redirect("all_books")
    else:
        form=BookForm(instance=books)
        
    return render(request,"update_books.html",{"form":form})