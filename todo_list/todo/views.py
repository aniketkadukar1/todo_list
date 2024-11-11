from django.shortcuts import render, redirect
from .models import Task
from .forms import NewTaskForm, UpdateTaskForm
from django.core.paginator import Paginator


def index(request):
    tasks = Task.objects.all()
    paginator = Paginator(tasks, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'todo/index.html', {'tasks' : tasks, 'page_obj' : page_obj})

def detail(request, pk):
    task = Task.objects.get(pk=pk)
    return render(request, 'todo/detail.html', {'task' : task})

def new(request):
    if request.method == 'POST':
        form = NewTaskForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/')
    else:
        form = NewTaskForm()
    return render(request, 'todo/new.html', {'form' : form})

def update(request, pk):
    task = Task.objects.get(pk=pk)

    if request.method == 'POST':
        form = UpdateTaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UpdateTaskForm(instance=task)

    return render(request, 'todo/update.html', {'task' : task, 'form' : form})

def delete(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return redirect('/')
