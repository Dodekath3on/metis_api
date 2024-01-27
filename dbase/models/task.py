from django.db import models
from datetime import date, timedelta

from .user import User
from .project import Project

class Task(models.Model):
  name = models.CharField(max_length=100)
  status = models.CharField(max_length=100)
  assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
  project = models.ForeignKey(Project, on_delete=models.CASCADE)
  priority = models.IntegerField()
  description = models.CharField(max_length=250, blank=True)

  due_date = models.DateField(default=date.today())
  estimated_time = models.DurationField(default=timedelta(days=1))
  actual_time = models.DurationField(default=timedelta(days=1))

  def __str__(self):
    return f"{self.name}"