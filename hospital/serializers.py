from rest_framework import serializers
from .models import hospital, department

class departmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = department
        fields = ('dept_name',)  # Assuming 'dept_name' is the full department name field

class hospitalSerializer(serializers.ModelSerializer):
    department_names = serializers.SerializerMethodField()

    class Meta:
        model = hospital
        fields = ( 'hospital_name', 'department_names')

    def get_department_names(self, obj):
        return [dept.dept_name for dept in obj.department.all()]