from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime
# Create your models here.




class Task(models.Model):
    PROJECT1 = 'PJ1'
    PROJECT2 = 'PJ2'
    PROJECT3 = 'PJ3'
    PROJECT4 = 'PJ4'
    PROJECT5 = 'PJ5'

    PROJECT_CHOICES = [
        (PROJECT1, 'PROJECT1'),
        (PROJECT2, 'PROJECT2'),
        (PROJECT3, 'PROJECT3'),
        (PROJECT4, 'PROJECT4'),
        (PROJECT5, 'PROJECT5'),
    ]
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    projectNo = models.CharField( max_length=10,choices=PROJECT_CHOICES,default=PROJECT1)
    taskName = models.CharField(unique=True, max_length = 30)
    startTime = models.TimeField(auto_now=False)
    timeTaken = models.CharField(max_length=10)
    endTime = models.TimeField(auto_now=True)

    def __str__(self):
        return self.taskName