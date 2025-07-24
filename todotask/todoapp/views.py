from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'home.html')
def taskpage(request):
    return render(request, 'task.html')