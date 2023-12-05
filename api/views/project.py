from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets

from dbase.models import Project
from ..serializers import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
  queryset = Project.objects.all()
  serializer_class = ProjectSerializer

'''
@api_view(['GET'])
def getProjects(request):
  projects = Project.objects.all()
  serializer = ProjectSerializer(projects, many=True)
  return Response(serializer.data)
'''