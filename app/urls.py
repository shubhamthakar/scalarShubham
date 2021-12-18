from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('taskManager/', TaskManagerView.as_view(), name="TaskManagerView"),
    path('displayTask/', getTaskView.as_view(), name="getTaskView"),
    path('accounts/login/', SignInView.as_view(), name="SignInView"),
    path('register/', RegistrationView.as_view(), name="RegistrationView"),
    path('signout/', SignOutView.as_view(), name="SignOutView"),
]   