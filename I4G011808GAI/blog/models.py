from re import X
from typing import Text
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User=get_user_model()

class Post(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    Title = models.CharField(max_length=200)
    Text = models.TextField()
    created_date = models.DateTimeField(default=datetime.now,blank=True)
    published_date = models.DateTimeField(default=datetime.now,blank=True)  