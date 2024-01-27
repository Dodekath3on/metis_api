from django.db import models
from .team import Team

class Project(models.Model):
  name = models.CharField(max_length=100)
  teams = models.ManyToManyField(Team)
  budget = models.DecimalField(
    max_digits=9,
    decimal_places=2,
    default=0.00,
    blank=True
  )

  def __str__(self):
    return f"{self.name}"
  
  def users(self):
    return list(set(self.user_set.all()))