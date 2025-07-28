from django.shortcuts import render
from django.contrib.auth.models import User
from .models import*
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def homepage(request):
    return render(request, 'home.html')
# def taskpage(request):
#     return render(request, 'task.html')
# def todoedit(request):
#     return render(request, 'todoedit.html')
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

def pagereg(request):
    if request.method=="POST":
    
        user=User.objects.create(username=request.POST.get("username"))
        user.set_password(request.POST.get("password"))
        user.save()
        Profile.objects.create(
            user=user,
            firstname=request.POST.get("firstname"),
            lastname=request.POST.get("lastname"),
            email=request.POST.get("Email"),
            phone=request.POST.get("num"),
            image=request.FILES["image"],
         )
        return HttpResponseRedirect(reverse(homepage))   
    


def addtodo(request):
    # todos=Todo.objects.filter(user=request.user)
    todos=Todo.objects.all()
    if request.method=="POST":
        Todo.objects.create(
            title=request.POST.get("title"),
            deadline=request.POST.get("deadline"),
            # user=request.user

        )
        return HttpResponseRedirect(reverse('addtodo'))
    print(f"todos {todos}")
    return render(request, 'task.html',{'content':todos})
def todocomplete(request,pk):
    todo=Todo.objects.filter(pk=pk).first()
    todo.complete=True
    todo.save()
    return HttpResponseRedirect(reverse('addtodo'))
def todoclose(request,pk):
    todoclosing=Todo.objects.filter(pk=pk).first()
    todoclosing.complete=False
    todoclosing.save()
    return HttpResponseRedirect(reverse('addtodo'))


def taskedit(request,pk):
    tasks=Todo.objects.filter(pk=pk).first()
    if request.method=="POST":
        tasks.title=request.POST.get("title")
        tasks.deadline=request.POST.get("deadline")
        tasks.save()
        return HttpResponseRedirect(reverse('addtodo'))
    return render(request, 'todoedit.html',{'content':tasks})


def taskdelete(request,pk):
    tasks=""
    tasks=Todo.objects.filter(pk=pk).first()
    print(tasks)
    tasks.delete()
    return HttpResponseRedirect(reverse('addtodo'))



