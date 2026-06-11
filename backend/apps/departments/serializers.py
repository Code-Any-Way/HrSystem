from rest_framework import serializers
from departments.models import Department

class DepartmentSerializer(serializers.ModelSerializer):
    company_name = serializers.ReadOnlyField(source='company.name')

    class Meta:
        model = Department
        fields = ['id', 'company', 'company_name', 'name', 'description', 'created_at', 'updated_at']
