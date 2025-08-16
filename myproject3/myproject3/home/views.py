from django.shortcuts import render,redirect
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello world")

def goreviki(request):
    context={"tittle":"Anasayfa","user":request.user}
    return render(request,"goreviki.html",context)

def gorevuc(request):
    return redirect("goreviki")