from rest_framework import serializers
from dbase.models import Team

class TeamSerializer(serializers.ModelSerializer):
  class Meta:
    model = Team
    fields = '__all__'