from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from .models import *
from django.forms import ModelForm, TextInput
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField


class CreateInterviewForm(forms.Form):

    choices = []
    users = User.objects.all()
    for user in users:
        ele = (user.username, user.username)
        choices.append(ele)

    title = forms.CharField(widget=forms.TextInput(attrs={'id':'title'}))
    startTime = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time', 'id':'startTime'}))
    endTime = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time', 'id':'endTime'}))
    participants = forms.MultipleChoiceField(
        required=True,
        widget=forms.CheckboxSelectMultiple(attrs={'id':'participants'}),
        choices=choices,
        
    )


# class TaskForm(forms.ModelForm):
    
#     class Meta:
#         model = Task
#         fields = ["projectNo","taskName","startTime","timeTaken"]
#         widgets = {
#             'timeTaken': forms.TextInput(attrs={'id': 'countdown', 'readonly': 'readonly'}),
#             'startTime':  forms.TextInput(attrs={'id': 'time1','readonly': 'readonly'})
#             }
        

# class SignInForm(forms.ModelForm):
    
#     class Meta:
#         model = User
#         fields = ["username", "password"]
#         widgets = {
#             'password' : forms.PasswordInput(attrs={'class': 'form-control'}),
#             'username': forms.TextInput(attrs={'class': 'form-control'}),
#             }

# class RegisterForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ["username", "password", "email"]
#         widgets = {
#             'password' : forms.PasswordInput(attrs={'class': 'form-control'}),
#             'username': forms.TextInput(attrs={'class': 'form-control'}),
#             'email': forms.TextInput(attrs={'class': 'form-control'}),
#             }
    # username = forms.CharField(label = 'Username', max_length = 12)
    # password = forms.CharField(label = 'Password',min_length = 6, widget = forms.PasswordInput(attrs={'class': 'form-control', 'style': 'width: 75%;'}))
    # email = forms.CharField(label = 'email', max_length = 20)

    # class CreateInterviewForm(forms.ModelForm):

#     choices = []
#     users = User.objects.all()
#     for user in users:
#         ele = (user.username, user.username)
#         choices.append(ele)

#     participants = forms.MultipleChoiceField(choices = choices)
#     class Meta:
#         model = Interview
#         fields = ["title", "startTime", "endTime"]
#         widgets = {
#             'endTime': forms.DateInput(format="%d/%m/%Y"),
#             'startTime':  forms.DateInput(format="%d/%m/%Y"),
#             'title': forms.TextInput(attrs={'value':1}),
#             }