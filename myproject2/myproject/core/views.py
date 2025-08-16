from django.http import HttpResponse
from django.shortcuts import render,redirect

def simple_text(request):
    return HttpResponse("a basic text page")
    


def simple_render(request):
    context={"tittle":"Merhaba","user":request.user}
    return render(request,"simple.html",context)

def simple_redirect(request):
    return redirect("simple_text")
