from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.http import HttpResponseNotFound


# Create your views here.

def delete_task(request, task_id):
    tasks = Task.objects.get(pk=task_id)
    tasks.delete()
    return redirect('home')


def update_task(request, task_id):
    tasks = Task.objects.get(pk=task_id)
    form = TaskForm(request.POST, instance=tasks)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'main/update_task.html',
                  {'tasks': tasks,
                   'form': form})


def show_task(request, task_id):
    tasks = Task.objects.get(pk=task_id)
    return render(request, 'main/show_task.html',
                  {'tasks': tasks})


def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html',
                  {'title': 'Главная страница сайта', 'tasks': tasks})


def about(request):
    return render(request, 'main/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)

