from rest_framework import serializers
from assets.models import Asset, AssetAssignment, AssetStatus
from employees.serializers import EmployeeMiniSerializer

class AssetSerializer(serializers.ModelSerializer):
    company_name = serializers.ReadOnlyField(source='company.name')

    class Meta:
        model = Asset
        fields = ['id', 'company', 'company_name', 'name', 'asset_type', 'serial_number', 'status', 'created_at', 'updated_at']

class AssetAssignmentSerializer(serializers.ModelSerializer):
    asset_details = AssetSerializer(source='asset', read_only=True)
    employee_details = EmployeeMiniSerializer(source='employee', read_only=True)

    class Meta:
        model = AssetAssignment
        fields = [
            'id', 'asset', 'asset_details', 'employee', 'employee_details', 
            'assigned_date', 'returned_date', 'condition_on_assignment', 
            'condition_on_return', 'created_at', 'updated_at'
        ]
