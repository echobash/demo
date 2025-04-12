from django.db import models


class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=30,default=None)
    completed = models.BooleanField(default=False)
