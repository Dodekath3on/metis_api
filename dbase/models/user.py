from django.db import models

class User(models.Model):
  name = models.CharField(max_length=100)
  username = models.CharField(max_length=100, unique=True)
  email = models.EmailField(max_length=100, unique=True)

  def __str__(self):
    return f"{self.username}"