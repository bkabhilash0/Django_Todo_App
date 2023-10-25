from django.db import models
from django.contrib.auth.models import  User


# Create your models here.

class Todo(models.Model):
    todo = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE)


