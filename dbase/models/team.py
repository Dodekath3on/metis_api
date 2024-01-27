from django.db import models
from .company import Company

class Team(models.Model):
  name = models.CharField(max_length=100)
  company = models.ForeignKey(Company, on_delete=models.CASCADE)

  def __str__(self) -> str:
    return f"{self.name}"
  