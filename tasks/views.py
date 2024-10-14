from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.utils import timezone
from .forms import TaskForm
from .models import Task


def home(request):
    """
    Home page view
    """
    return render(request, 'home.html')

# authentication views


def signup(request):
    """
    Signup view
        """

    if request.method == 'GET':
        return render(request, 'signup.html',
                      {
                          'form': UserCreationForm
                      })
    else:
        if request.POST['password1'] == request.POST['password2']:
            # register user
            try:
                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('tasks')
            except IntegrityError:
                return render(request, 'signup.html',
                              {
                                  'form': UserCreationForm,
                                  'error': 'Username already exists'
                              })

        return render(request, 'signup.html',
                      {
                          'form': UserCreationForm,
                          'error': 'Passwords did not match'
                      })


@login_required
def logout_user(request):
    """
    Logout view
    """
    logout(request)
    return redirect('home')


def login_user(request):
    """
    Login view
    """
    if request.method == 'GET':
        return render(request, 'login.html',
                      {
                          'form': AuthenticationForm
                      })
    else:
        user = authenticate(request, username=request.POST['username'],
                            password=request.POST['password'])
        if user is None:
            return render(request, 'login.html',
                          {
                              'form': AuthenticationForm,
                              'error': 'Username or password did not match'
                          })
        else:
            login(request, user)
            return redirect('tasks')

# task views


@login_required
def tasks(request):
    """
    Tasks view for authenticated users - GET(READ)
    """
    tasks = Task.objects.filter(user=request.user, date_completed__isnull=True)
    return render(request, 'tasks.html',
                  {
                      'tasks': tasks
                  })


@login_required
def tasks_completed(request):
    """
    Tasks completed view for authenticated users - GET(READ)
    """
    tasks = Task.objects.filter(
        user=request.user, date_completed__isnull=False).order_by('-date_completed')
    return render(request, 'tasks.html',
                  {
                      'tasks': tasks
                  })


@login_required
def task_detail(request, task_id):
    """
    Task detail view - GET(READ) and POST(UPDATE)
    """
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'GET':
        form = TaskForm(instance=task)
        return render(request, 'task_detail.html',
                      {
                          'task': task,
                          'form': form
                      })
    else:
        try:
            form = TaskForm(request.POST, instance=task).save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'task_detail.html',
                          {
                              'task': task,
                              'form': TaskForm,
                              'error': 'Bad data passed in. Try again'
                          })


@login_required
def create_task(request):
    """
    Create task view - POST(CREATE)
    """
    if request.method == 'GET':
        return render(request, 'create_task.html',
                      {
                          'form': TaskForm
                      })
    else:
        try:
            form = TaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'create_task.html',
                          {
                              'form': TaskForm,
                              'error': 'Bad data passed in. Try again'
                          })


@login_required
def complete_task(request, task_id):
    """
    Complete task view - POST(UPDATE)
    """
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.date_completed = timezone.now()
        task.save()
        return redirect('tasks')


@login_required
def delete_task(request, task_id):
    """
    Delete task view - POST(DELETE)
    """
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks')
