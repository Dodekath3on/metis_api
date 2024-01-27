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
  
  def hours(self):
    tasks = self.task_set.all()
    hours_billed = 0
    for task in tasks:
      hours_billed += task.estimated_time.days * 8
    return hours_billed
  
  def remaining_budget(self):
    remaining_budget = self.budget
    tasks = self.task_set.all()
    for task in tasks:
      remaining_budget -= task.estimated_time.days * 8 * task.assigned_to.bill_rate
    return remaining_budget
  
  def remaining_budget_percentage(self):
    return f'{int((self.remaining_budget() / self.budget) * 100)}%'