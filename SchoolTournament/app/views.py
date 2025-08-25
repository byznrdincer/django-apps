from django.shortcuts import render,redirect,get_object_or_404
from . models import Student,Match,Team
from . forms import StudentForm,MatchForm,TeamForm

def add_student(request):
    if request.method=="POST":
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("all_student")
    else:
        form=StudentForm()
    return render(request,"add_student.html",{"form":form})

def all_student(request):
    student=Student.objects.all()
    return render(request,"all_student.html",{"student":student})

def delete_student(request,pk):
    student=get_object_or_404(Student,pk=pk)
    student.delete()
    return redirect("all_student")

def update_student(request,pk):
    student=get_object_or_404(Student,pk=pk)
    if request.method=="POST":
        form=StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect("all_student")
    else:
        form=StudentForm(instance=student)
    return render(request,"update_student.html",{"form":form})


def add_match(request):
    if request.method=="POST":
        form=MatchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("all_match")
    else:
        form=MatchForm()
    return render(request,"add_match.html",{"form":form})

def all_match(request):
    match=Match.objects.all()
    return render(request,"all_match.html",{"match":match})

def delete_match(request,pk):
    match=get_object_or_404(Match,pk=pk)
    match.delete()
    return redirect("all_match")

def update_match(request,pk):
    match=get_object_or_404(Match,pk=pk)
    if request.method=="POST":
        form=MatchForm(request.POST,instance=match)
        if form.is_valid():
           form.save()
           return redirect("all_match")
    else:
        form=MatchForm(instance=match)
    
    return render(request,"update_match.html",{"form":form})




def add_team(request):
    if request.method=="POST":
        form=TeamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("all_team")
    else:
        form=TeamForm()
    return render(request,"add_team.html",{"form":form})

def delete_team(request,pk):
    team=get_object_or_404(Team,pk=pk)
    team.delete()
    return redirect("all_team")

def all_team(request):
    team=Team.objects.all()
    return render(request,"all_team.html",{"team":team})

def update_team(request,pk):
    team=get_object_or_404(Team,pk=pk)
    if request.method=="POST":
        form=TeamForm(request.POST,instance=team)
        if form.is_valid():
           form.save()
           return redirect("all_team")
    else:
        form=TeamForm(instance=team)
    return render(request,"update_team.html",{"form":form})

