from django.db import models
from .team import Team

class Project(models.Model):
  name = models.CharField(max_length=100)
  teams = models.ManyToManyField(Team)

  def __str__(self):
    return f"{self.name}"
  
  def users(self):
    return list(set(self.user_set.all()))