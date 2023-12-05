from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets

from dbase.models import Task
from ..serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
  queryset = Task.objects.all()
  serializer_class = TaskSerializer

@api_view(['GET'])
def getUserTasks(request, user_id):
  tasks = Task.objects.filter(assigned_to=user_id)
  serializer = TaskSerializer(tasks, many=True)
  return Response(serializer.data)

'''
@api_view(['GET'])
def getTasks(request):
  tasks = Task.objects.all()
  serializer = TaskSerializer(tasks, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def getTask(request, task_id):
  tasks = Task.objects.filter(id=task_id)
  serializer = TaskSerializer(tasks, many=True)
  return Response(serializer.data)
'''