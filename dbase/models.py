from django.db import models
  
class User(models.Model):
  name = models.CharField(max_length=100)
  username = models.CharField(max_length=100, unique=True)
  email = models.EmailField(max_length=100, unique=True)

  def __str__(self):
    return f"{self.username}"
  

class Project(models.Model):
  name = models.CharField(max_length=100)

  def __str__(self):
    return f"{self.name}"
  

class Task(models.Model):
  name = models.CharField(max_length=100)
  status = models.CharField(max_length=100)
  assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
  project = models.ForeignKey(Project, on_delete=models.CASCADE)
  priority = models.IntegerField()

  def __str__(self):
    return f"{self.name} - {self.assigned_to.name}"


  # tasks = models.ManyToManyField(
  #   Task,
  #   through="Task",
  #   through_fields=("user", "project")
  # )
  # tasks = models.ManyToManyField(
  #   Task,
  #   through="Task",
  #   through_fields=("project", "user")
  # )