from django.shortcuts import render
from mainapp.forms import studentform
def home(request):
    return render(request,"school.html")

def dashboard(request):
    fm=studentform
    return render(request,"dashboard.html",{"form":fm})