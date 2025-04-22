from rest_framework import serializers
from . import models

class StudentSerializer(serializers.ModelSerializers):
    class Meta:
        model = models.Student
        fields = ['name', 'id', 'age', 'course']