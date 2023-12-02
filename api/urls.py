from django.urls import path
from .views import user
from .views import project
from .views import task

urlpatterns = [
  path('user/<int:user_id>', user.showUser),
  path('user/tasks/<int:user_id>', user.getUserTasks),
]