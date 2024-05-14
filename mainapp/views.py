from django.shortcuts import render
from . forms import registrationForm,Userloginform

def index(request):
    return render(request, "index.html")

def registrations(request):
    fm=registrationForm()
    return render(request, "home.html",{"form":fm})

def userlogin(request):
    fm=Userloginform()
    return render(request,"loginform.html",{"form":fm})