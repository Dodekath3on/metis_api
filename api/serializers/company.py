from rest_framework import serializers
from dbase.models import Company

class CompanySerializer(serializers.ModelSerializer):
  class Meta:
    model = Company
    fields = '__all__'