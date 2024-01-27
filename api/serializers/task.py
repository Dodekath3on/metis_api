from rest_framework import serializers
from dbase.models import Task
from .user import UserSerializer

class TaskSerializer(serializers.ModelSerializer):
  assigned_to = UserSerializer()
  class Meta:
    model = Task
    fields = '__all__'