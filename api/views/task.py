from rest_framework.response import Response
from rest_framework.decorators import api_view

from dbase.models import Task
from ..serializers import TaskSerializer

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