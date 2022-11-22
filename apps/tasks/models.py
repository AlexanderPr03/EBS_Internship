from django.db import models
from apps.users.models import User
# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=200, unique=False, default="Task Name")
    description = models.CharField(max_length=1000, blank=True, default="Task Description")
    status = models.BooleanField(default=False)
    assignee = models.ForeignKey(User, on_delete=models.CASCADE)

