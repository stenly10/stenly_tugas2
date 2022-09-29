import re
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from todolist.forms import FormForTask
from todolist.models import Task

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    list_task = Task.objects.all()
    context = {
        'user': request.user,
        'username': request.user.get_username(),
        'list_task': list_task,
        'last_login': request.COOKIES['last_login']
    }
    return render(request, "todolist.html", context)

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')

    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("todolist:show_todolist"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Username atau Password  salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

def create_task(request):
    form = FormForTask()
    if request.method == "POST":
        form = FormForTask(request.POST)
        if form.is_valid:
            task = Task()
            task.title = form['title'].value()
            task.user = request.user
            task.description = form['description'].value()
            task.date = datetime.datetime.now()
            task.save()
            return redirect('todolist:show_todolist')
        else:
            messages.info(request, 'Mohon mengisi text field')
    context = {'form':form}
    return render(request, 'create_task.html', context)

def change_status(request):
    list_task = Task.objects.all()
    for task in list_task:
        if request.POST.get(str(task.id)):
            task.is_finished = not task.is_finished
            task.save()
    return redirect('todolist:show_todolist')

def delete_task(request):
    list_task = Task.objects.all()
    for task in list_task:
        if request.POST.get(str(task.id)):
            task.delete()
    return redirect('todolist:show_todolist')
            


