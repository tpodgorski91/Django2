from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'tasks/home.html')


def task(request):
    return render(request, 'tasks/activity.html')
