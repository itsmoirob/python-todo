from django.shortcuts import redirect, render

from .models import *
from .forms import *

# Create your views here.


def index(request):
    """
    GET: View all tasks
    POST: Create new task
    """

    tasks = Task.objects.all()

    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('/')

    context = {'tasks': tasks, 'form': form}
    return render(request, 'tasks/list.html', context)


def updateTask(request, pk):
    """
    Updates a task
    """

    task = Task.objects.get(id=pk)

    return render(request, 'tasks/update_task.html')
