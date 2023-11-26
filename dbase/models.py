from django.db import models

class User(models.Model):
  name = models.CharField(max_length=100)
  username = models.CharField(max_length=100, unique=True)
  email = models.EmailField(max_length=100, unique=True)

class Project(models.Model):
  name = models.CharField(max_length=100)

class Task(models.Model):
  name = models.CharField(max_length=100)
  status = models.CharField(max_length=100)
  assigned_to = models.ForeignKey(User)
  project = models.ForeignKey(Project)
  priority = models.IntegerField()