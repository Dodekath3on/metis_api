from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets

from dbase.models import Team
from ..serializers import TeamSerializer

class TeamViewSet(viewsets.ModelViewSet):
  queryset = Team.objects.all()
  serializer_class = TeamSerializer