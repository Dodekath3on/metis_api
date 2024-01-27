from django.db import models
from .project import Project
from .team import Team

class User(models.Model):
  name = models.CharField(max_length=100)
  username = models.CharField(max_length=100, unique=True)
  email = models.EmailField(max_length=100, unique=True)
  project_set = models.ManyToManyField(Project, through='Task')
  teams = models.ManyToManyField(Team)
  bill_rate = models.DecimalField(
    max_digits=5,
    decimal_places=2,
    default=0.00,
  )

  def __str__(self) -> str:
    return f"{self.username}"
  
  def projects(self) -> list:
    return list(set(self.project_set.all()))
  
  def tasks(self) -> list:
    return self.task_set.all()