from typing import ChainMap
from django.db import models
from django.db.models.fields import CharField, TextField

class Poll(models.Model):
    question = TextField()
    one = models.CharField(max_length=50)
    two = models.CharField(max_length=50)
    three = models.CharField(max_length=50)
    one_count = models.IntegerField(default=0)
    two_count = models.IntegerField(default=0)
    three_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


