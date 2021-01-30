from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('Home site')


def task(request):
    return render(request, 'tasks/activity.html')
