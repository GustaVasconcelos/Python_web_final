from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def index(request,name):
    now = datetime.datetime.now()
    return render(request,"hello/index.html",{
        "name":name.capitalize()
    })
