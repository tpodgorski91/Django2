from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *


def home(request):
    return render(request, 'tasks/home.html')


def tasks_list(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'tasks/activity.html', context)


def task_create(request):
    new = Task.objects.all()
    new_form = TaskForm()
    if request.method == 'POST':
        new_form = TaskForm(request.POST)
        if new_form.is_valid():
            new_form.save()
        return redirect('/tasks/')
    context = {'form': new_form}
    return render(request, 'tasks/task_create.html', context)


def edit(request, pk):
    goal = Task.objects.get(id=pk)
    update_form = TaskForm(instance=goal)
    if request.method == 'POST':
        update_form = TaskForm(request.POST, instance=goal)
        if update_form.is_valid():
            update_form.save()
        return redirect('/tasks/')
    context = {'form': update_form}
    return render(request, 'tasks/edit.html', context)


def task_delete(request, pk):
    item = Task.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/tasks/')
    context = {'item': item}
    return render(request, 'tasks/task_delete.html', context)
