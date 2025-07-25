from django.urls import path
from .import views

urlpatterns = [
    path('',views.homepage,name="homepage"),
    path('taskpage/',views.taskpage, name="taskpage"),
    path('todoedit/',views.todoedit, name="todoedit"),
    path('pagelogin/',views.pagelogin, name="pagelogin"),
    path('logout', views.userlogout,name="logout"),
]