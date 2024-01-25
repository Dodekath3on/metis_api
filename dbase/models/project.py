from django.db import models
from .team import Team

class Project(models.Model):
  name = models.CharField(max_length=100)
  team = models.ManyToManyField(Team)

  def __str__(self):
    return f"{self.name}"