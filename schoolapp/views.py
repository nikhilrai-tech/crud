from django.shortcuts import render,HttpResponseRedirect
from mainapp.forms import studentform
from django.contrib.auth.decorators import login_required
from mainapp.models import Student

def home(request):
    return render(request,"school.html")

@login_required
def dashboard(request):
    if request.method=="POST":
        fm=studentform(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect("/school/dashboard/")
    fm=studentform()
    data=Student.objects.all()
    return render(request,"dashboard.html",{"form":fm,"data":data})


@login_required
def update(request,pk):
    id=Student.objects.get(id=pk)
    if request.method=="POST":
        fm=studentform(data=request.POST,instance=id)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect("/school/dashboard/")
    fm=studentform(instance=id)
    return render(request,"update.html",{"form":fm})

@login_required
def delete(request, pk):
    id=pk
    if request.method == "POST":
        stu=Student.objects.get(id=id)
        stu.delete()
        return HttpResponseRedirect("/school/dashboard/")
