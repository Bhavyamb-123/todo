from django.shortcuts import render
from django.contrib.auth.models import User
from .models import*
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def homepage(request):
    return render(request, 'home.html')
def taskpage(request):
    return render(request, 'task.html')
def todoedit(request):
    return render(request, 'todoedit.html')
def  pagelogin(request):
    msg=""
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            print("login successfully")
            return HttpResponseRedirect(reverse("homepage"))
        else:
            print("User not found")
            msg="invalid credentials"
        print(username,password)
    return render(request,'home.html', {"msg":msg})
def userlogout(request):
    logout(request)
    return HttpResponseRedirect(reverse(homepage))