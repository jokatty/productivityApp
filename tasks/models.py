from pyexpat import model
from turtle import title
from django.db import models

class Tasks(models.Model):
  title = models.CharField(max_length=120)
  description = models.CharField(max_length=1000)
  completed = models.BooleanField(default=False)

  def __str__(self):
    return self.title


