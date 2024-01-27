from rest_framework import serializers
from dbase.models import Project
from .team import TeamSerializer

class ProjectSerializer(serializers.ModelSerializer):
  teams = TeamSerializer(many = True)
  class Meta:
    model = Project
    fields = '__all__'