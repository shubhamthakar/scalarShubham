from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from .models import *
from django.forms import ModelForm, TextInput


class TaskForm(forms.ModelForm):
    
    class Meta:
        model = Task
        fields = ["projectNo","taskName","startTime","timeTaken"]
        widgets = {
            'timeTaken': forms.TextInput(attrs={'id': 'countdown', 'readonly': 'readonly'}),
            'startTime':  forms.TextInput(attrs={'id': 'time1','readonly': 'readonly'})
            }
        

class SignInForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ["username", "password"]
        widgets = {
            'password' : forms.PasswordInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            }

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password", "email"]
        widgets = {
            'password' : forms.PasswordInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            }
    # username = forms.CharField(label = 'Username', max_length = 12)
    # password = forms.CharField(label = 'Password',min_length = 6, widget = forms.PasswordInput(attrs={'class': 'form-control', 'style': 'width: 75%;'}))
    # email = forms.CharField(label = 'email', max_length = 20)