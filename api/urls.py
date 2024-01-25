from rest_framework.routers import DefaultRouter

from django.urls import path, include

from .views import user
from .views import project
from .views import task
from .views import team
from .views import company

'''
TODO: Create separate url files for respective models
This file may get overpopulated and messy with full
RESTful routes and the addition of later models.
'''

router = DefaultRouter()
router.register(r'user', user.UserViewSet)
router.register(r'project', project.ProjectViewSet)
router.register(r'task', task.TaskViewSet)
router.register(r'team', team.TeamViewSet)
router.register(r'company', company.CompanyViewSet)


urlpatterns = [
  path('', include(router.urls)),
  path('task/user/<int:user_id>', task.getUserTasks),
]

'''
  # Users
  path('users/', user.getUsers),
  path('users/<int:user_id>', user.showUser),
  path('users/tasks/<int:user_id>', user.getUserTasks),
  path('users/new', user.addUser),
  path('users/delete/<int:user_id>', user.destroyUser),


  # Tasks
  path('tasks/', task.getTasks),
  path('tasks/<int:task_id>', task.getTask),

  # Projects
  # path('projects/', project.getProjects),
  # path('projects/<int:project_id>', project.getProject),

'''