from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets

from dbase.models import User
from ..serializers import UserSerializer
from ..serializers import TaskSerializer

class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer



'''
@api_view(['GET']) # INDEX
def getUsers(request):
  user = User.objects.all()
  serializer = UserSerializer(user, many=True)
  return Response(serializer.data)

@api_view(['GET']) # SHOW
def showUser(request, user_id):
  user = User.objects.filter(id=user_id)
  serializer = UserSerializer(user, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def getUserTasks(request, user_id):
  user = User.objects.get(id=user_id)
  serializer = TaskSerializer(user.task_set.all(), many=True)
  return Response(serializer.data)

@api_view(['POST'])
def addUser(request):
  serializer = UserSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data)
  
@api_view(['DELETE'])
def destroyUser(request, user_id):
  user = User.objects.filter(id=user_id)
  if user:
    user.delete()
  return Response(request)

'''
