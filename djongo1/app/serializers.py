from rest_framework import serializers
from .models import employees

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = employees
        fields =('emp_id','firstName','lastName')

