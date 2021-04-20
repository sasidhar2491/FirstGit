from rest_framework import serializers
from .models import StudentData,groupdata


class groupserializer(serializers.ModelSerializer):
    class Meta:
        model = groupdata
        fields='__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentData
        fields = '__all__'

