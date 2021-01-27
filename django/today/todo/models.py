from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Todo(models.Model):
    text = models.CharField(max_length=100)
    addedon = models.DateTimeField(auto_now_add=True)


class UserTodo(models.Model):
    text = models.CharField(max_length=100)
    addedon = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
