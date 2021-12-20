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
from datetime import datetime



class CreateInterview(View):
    def get(self, request):
        form = CreateInterviewForm()
        context = {"form":form}
        return render(request, 'create.html', context)
    def post(self, request):
        form = CreateInterviewForm(request.POST)
        if form.is_valid():
            participants = form.cleaned_data.get("participants")
            title = form.cleaned_data.get('title')
            startTime = request.POST.get('startTime')
            endTime = request.POST.get('endTime')
            if len(participants) < 2:
                messages.info(request, 'Add atleast 2 members')
                return redirect('CreateInterview')
            now = datetime.now()
            currentTime = now.strftime("%H:%M")
            print("Current Time =", currentTime)
            print("StartTIme",startTime)
            print("StartTIme",endTime)
            if endTime < currentTime or startTime < currentTime:
                messages.info(request, 'Input correct start and end time')
                return redirect('CreateInterview')
            if endTime < startTime:
                messages.info(request, 'Input correct end time')
                return redirect('CreateInterview')
            
            for name in participants:
                user = User.objects.get(username=name)
                participantObjArr = Participant.objects.filter(user=user)
                for ele in participantObjArr:
                    start = ele.interview.startTime
                    end = ele.interview.endTime
                    if startTime > str(start) and startTime < str(end):
                        messages.info(request, 'Timings clashing')
                        return redirect('CreateInterview')
                    if endTime > str(start) and endTime < str(end):
                        messages.info(request, 'Timings clashing')
                        return redirect('CreateInterview')
            interview = Interview.objects.create(title=title, startTime=startTime, endTime=endTime)
            for name in participants:
                user = User.objects.get(username = name)
                Participant.objects.create(interview=interview, user=user)

            return redirect('DisplayInterviews')
                    



        


class DisplayInterviews(View):
    def get(self, request):
        interviews = Interview.objects.all().order_by("startTime")
        arr = []
        for i in interviews:
            data = {}
            data['id'] = i.id
            data['title'] = i.title
            data['startTime'] = i.startTime
            data['endTime'] = i.endTime
            data['participants'] = []
            participants = Participant.objects.filter(interview=i)
            for j in participants:
                data['participants'].append(j.user.username)
            arr.append(data)
        print(arr)
        return render(request, 'display.html', {"data":arr})



class EditInterviews(View):
    def get(self, request, pk):
        interview = Interview.objects.get(id=pk)
        participants = Participant.objects.filter(interview=interview)
        users = []
        for ele in participants:
            users.append(ele.user.username)
        form = CreateInterviewForm()
        context = {"interview":interview, "users":users, "form":form}
        return render(request, 'edit.html', context)
    def post(self, request, pk):
        form = CreateInterviewForm(request.POST)
        if form.is_valid():
            participants = form.cleaned_data.get("participants")
            title = form.cleaned_data.get('title')
            startTime = request.POST.get('startTime')
            endTime = request.POST.get('endTime')
            if len(participants) < 2:
                messages.info(request, 'Add atleast 2 members')
                return redirect('EditInterviews', pk=pk)
            now = datetime.now()
            currentTime = now.strftime("%H:%M")
            print("Current Time =", currentTime)
            print("StartTIme",startTime)
            print("StartTIme",endTime)
            if endTime < currentTime or startTime < currentTime:
                messages.info(request, 'Input correct start and end time')
                return redirect('EditInterviews', pk=pk)
            if endTime < startTime:
                messages.info(request, 'Input correct end time')
                return redirect('EditInterviews', pk=pk)
            interview = Interview.objects.get(id=pk)
            for name in participants:
                user = User.objects.get(username=name)
                participantObjArr = Participant.objects.filter(user=user)
                for ele in participantObjArr:
                    if ele.interview == interview:
                        continue
                    else:
                        print(ele.interview)
                        print(interview)
                        start = ele.interview.startTime
                        end = ele.interview.endTime
                        if startTime > str(start) and startTime < str(end):
                            messages.info(request, 'Timings clashing')
                            return redirect('EditInterviews', pk=pk)
                        if endTime > str(start) and endTime < str(end):
                            messages.info(request, 'Timings clashing')
                            return redirect('EditInterviews', pk=pk)
            interview = Interview.objects.get(id=pk)
            interview.title = title
            interview.startTime = startTime
            interview.endTime = endTime
            interview.save()
            partObjArr = Participant.objects.filter(interview=interview)
            for ele in partObjArr:
                ele.delete()
            for name in participants:
                user = User.objects.get(username = name)
                Participant.objects.create(interview=interview, user=user)

            return redirect('DisplayInterviews')





















# @method_decorator(login_required, name='dispatch')
# class TaskManagerView(View):
#     def get(self, request):
#         form = TaskForm()
#         return render(request, 'task.html', {"form":form})
#     def post(self, request):
#         projectNo = request.POST.get('projectNo')
#         taskName = request.POST.get('taskName')
#         startTime = request.POST.get('startTime')
#         timeTaken = request.POST.get('timeTaken')
#         print(startTime[0:7])
#         startTime = datetime.datetime.strptime(startTime[0:7],"%H:%M:%S")
#         #timeTaken = datetime.datetime.strptime(timeTaken,"%H:%M:%S")
#         user = request.user
#         print(user)
#         task = Task.objects.create(user=user,projectNo=projectNo,taskName= taskName,startTime=startTime,timeTaken=timeTaken)
#         task.save()
#         messages.success(request, 'Task ' + taskName + 'was added')
#         return redirect('TaskManagerView')

# @method_decorator(login_required, name='dispatch')
# class getTaskView(View):
#     def get(self,request):
#         user = request.user
#         tasks = Task.objects.filter(user=user)
#         return render(request, 'displaytask.html', {"tasks":tasks})

    

# class SignInView(View):
#     def get(self,request):
#         if request.user.is_authenticated:
#             return redirect('TaskManagerView')
#         form = SignInForm()
#         return render(request, 'signin.html', {"form":form})

#     def post(self,request):
#         if request.user.is_authenticated:
#             return redirect('TaskManagerView')

#         username = request.POST.get('username')
#         password =request.POST.get('password')

#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             login(request, user)
#             return redirect('TaskManagerView')
#         else:
#             messages.info(request, 'Username OR password is incorrect')
#             return redirect('SignInView')

# class RegistrationView(View):
#     def get(self,request):
#         if request.user.is_authenticated:
#             return redirect('TaskManagerView')
#         form = RegisterForm()
#         return render(request, 'registration.html', {"form":form})

#     def post(self,request):
#         form = RegisterForm(request.POST)
#         if form.is_valid():
            
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             email = form.cleaned_data.get('email')
#             user = User.objects.create_user(username=username,email= email,password=password)
#             user.save()
#             messages.success(request, 'Account was created for ' + username)
#             return redirect('SignInView')
#         return render(request, 'registration.html', {"form":form})
        

# class SignOutView(View):
    
#     def get(self,request):
#         logout(request)
#         return redirect('SignInView')



