from django.shortcuts import render,redirect
from django.http import HttpResponse

def home(request):
    return redirect('greeting')

def greeting(request):
    context={"title":"greeting","user":request.user}
    return render(request,"home/greeting.html",context)
