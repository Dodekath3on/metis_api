from django.db import models
from .project import Project
from .team import Team

class User(models.Model):
  name = models.CharField(max_length=100)
  username = models.CharField(max_length=100, unique=True)
  email = models.EmailField(max_length=100, unique=True)
  project_set = models.ManyToManyField(Project, through='Task')
  teams = models.ManyToManyField(Team)

  def __str__(self):
    return f"{self.username}"
  
  def projects(self):
    return list(set(self.project_set.all()))
  
  def tasks(self):
    return self.task_set.all()