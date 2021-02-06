from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *


def home(request):
    return render(request, 'tasks/home.html')


def task(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/tasks/')

    context = {'tasks': tasks, 'form': form}
    return render(request, 'tasks/activity.html', context)


def edit(request, pk):
    goal = Task.objects.get(id=pk)
    form = TaskForm(instance=goal)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=goal)
        if form.is_valid():
            form.save()
        return redirect('/tasks/')

    context = {'form': form}

    return render(request, 'tasks/edit.html', context)


def task_delete(request, pk):
    item = Task.objects.get(id=pk)

    context = {'item': item}

    return render(request, 'tasks/task_delete.html', context)
