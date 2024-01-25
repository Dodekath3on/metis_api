from rest_framework import serializers
from dbase.models import User, Project, Task, Team, Company

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
  assigned_to = UserSerializer()
  class Meta:
    model = Task
    # fields = ['id', 'name', 'status','assigned']
    fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):
  class Meta:
    model = Company
    fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
  class Meta:
    model = Team
    fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
  team = TeamSerializer(many = True)
  class Meta:
    model = Project
    fields = '__all__'

