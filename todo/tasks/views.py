from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def home(request):
    return render(request, 'tasks/home.html')


def task(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'tasks/activity.html', context)
