from django.shortcuts import render,redirect,get_object_or_404
from . models import Album
from . forms import AlbumForm
from django.contrib import messages

#create
def add_album(request):
    if request.method=="POST":
        forms=AlbumForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.success(request,"saved successfully")
            return redirect('list_album')
    else:
        forms=AlbumForm()
    return render(request,'add_album.html',{'forms':forms})
#list
def list_album(request):
    albums=Album.objects.all()
    return render(request,"list_album.html",{"albums":albums})
#delete
def delete_album(request,pk):
    albums=get_object_or_404(Album,pk=pk)
    albums.delete()
    return redirect("list_album")

#update
def update_album(request,pk):
    albums=get_object_or_404(Album,pk=pk)
    if request.method=="POST":
        forms=AlbumForm(request.POST,instance=albums)
        if forms.is_valid():
            forms.save()
            return redirect("list_album")
    else:
        forms=AlbumForm(instance=albums)
    return render(request,"update_album.html",{"forms":forms})

        



