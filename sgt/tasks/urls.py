from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path('addtask/', views.add_task, name="add_task"),
    path('deltask/', views.del_task, name="del_task")

]

