from django.urls import path
from .import views

urlpatterns = [
    path('',views.homepage,name="homepage"),
    # path('taskpage/',views.taskpage, name="taskpage"),
    # path('todoedit/',views.todoedit, name="todoedit"),
    path('pagelogin/',views.pagelogin, name="pagelogin"),
    path('logout', views.userlogout,name="logout"),
    path('addtodo/', views.addtodo,name="addtodo"),
    path('todocomplete/<int:pk>', views.todocomplete,name="todocomplete"),
    path('todoclose/<int:pk>', views.todoclose,name="todoclose"),
    path('taskedit/<int:pk>', views.taskedit,name="taskedit"),
    path('taskdelete/<int:pk>',views.taskdelete,name="taskdelete"),
    

]