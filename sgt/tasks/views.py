from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Task


def index(request):
    tasks = Task.objects.all()
    return render(request, "tasks/index.html",{
        'tasks':tasks
    })
        
def add_task(request):
    if request.method == 'POST':
        tarefa = request.POST.get('tarefa')

        task = Task(tarefa = tarefa)

        task.save()

    return redirect('index')


def del_task(request):
    if request.method == 'POST':

        id_task = int(request.POST.get('del-task'))

        task = Task.objects.filter(id = id_task)

        task.delete()
    
    return redirect('index')