from django.shortcuts import render,redirect,get_object_or_404
from . models import Student
from . forms import StudentForm

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
    students=Student.objects.all()
    return render(request,"all_student.html",{"students":students})

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

def delete_student(request,pk):
    student=get_object_or_404(Student,pk=pk)
    student.delete()
    return redirect("all_student")
