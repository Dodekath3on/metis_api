from django.db import models
from .user import User
from .project import Project

class Task(models.Model):
  name = models.CharField(max_length=100)
  status = models.CharField(max_length=100)
  assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
  project = models.ForeignKey(Project, on_delete=models.CASCADE)
  priority = models.IntegerField()

  def __str__(self):
    return f"{self.name} - {self.assigned_to.name}"