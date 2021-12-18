from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import *
import time
import datetime
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required



@method_decorator(login_required, name='dispatch')
class TaskManagerView(View):
    def get(self, request):
        form = TaskForm()
        return render(request, 'task.html', {"form":form})
    def post(self, request):
        projectNo = request.POST.get('projectNo')
        taskName = request.POST.get('taskName')
        startTime = request.POST.get('startTime')
        timeTaken = request.POST.get('timeTaken')
        print(startTime[0:7])
        startTime = datetime.datetime.strptime(startTime[0:7],"%H:%M:%S")
        #timeTaken = datetime.datetime.strptime(timeTaken,"%H:%M:%S")
        user = request.user
        print(user)
        task = Task.objects.create(user=user,projectNo=projectNo,taskName= taskName,startTime=startTime,timeTaken=timeTaken)
        task.save()
        messages.success(request, 'Task ' + taskName + 'was added')
        return redirect('TaskManagerView')

@method_decorator(login_required, name='dispatch')
class getTaskView(View):
    def get(self,request):
        user = request.user
        tasks = Task.objects.filter(user=user)
        return render(request, 'displaytask.html', {"tasks":tasks})

    

class SignInView(View):
    def get(self,request):
        if request.user.is_authenticated:
            return redirect('TaskManagerView')
        form = SignInForm()
        return render(request, 'signin.html', {"form":form})

    def post(self,request):
        if request.user.is_authenticated:
            return redirect('TaskManagerView')

        username = request.POST.get('username')
        password =request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('TaskManagerView')
        else:
            messages.info(request, 'Username OR password is incorrect')
            return redirect('SignInView')

class RegistrationView(View):
    def get(self,request):
        if request.user.is_authenticated:
            return redirect('TaskManagerView')
        form = RegisterForm()
        return render(request, 'registration.html', {"form":form})

    def post(self,request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            email = form.cleaned_data.get('email')
            user = User.objects.create_user(username=username,email= email,password=password)
            user.save()
            messages.success(request, 'Account was created for ' + username)
            return redirect('SignInView')
        return render(request, 'registration.html', {"form":form})
        

class SignOutView(View):
    
    def get(self,request):
        logout(request)
        return redirect('SignInView')



