from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    # path('taskManager/', TaskManagerView.as_view(), name="TaskManagerView"),
    # path('displayTask/', getTaskView.as_view(), name="getTaskView"),
    # path('accounts/login/', SignInView.as_view(), name="SignInView"),
    # path('register/', RegistrationView.as_view(), name="RegistrationView"),
    # path('signout/', SignOutView.as_view(), name="SignOutView"),
    path('create/', CreateInterview.as_view(), name="CreateInterview"),
    path('display/', DisplayInterviews.as_view(), name="DisplayInterviews"),
    path('edit/<int:pk>/', EditInterviews.as_view(), name="EditInterviews")

]   