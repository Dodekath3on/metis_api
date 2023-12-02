from rest_framework.response import Response
from rest_framework.decorators import api_view

from dbase.models import User
from dbase.models import Task
from ..serializers import UserSerializer
from ..serializers import TaskSerializer

@api_view(['GET']) # SHOW
def showUser(request, user_id):
  user = User.objects.filter(id=user_id)
  serializer = UserSerializer(user, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def getUserTasks(request, user_id):
  user = User.objects.get(id=user_id)
  serializer = UserSerializer(user.task_set.all(), many=True)
  return Response(serializer.data)


