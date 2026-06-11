from rest_framework import serializers
from companies.models import Company, Branch

class BranchSerializer(serializers.ModelSerializer):
    company_name = serializers.ReadOnlyField(source='company.name')

    class Meta:
        model = Branch
        fields = ['id', 'company', 'company_name', 'name', 'email', 'phone', 'address', 'created_at', 'updated_at']

class CompanySerializer(serializers.ModelSerializer):
    branches = BranchSerializer(many=True, read_only=True)

    class Meta:
        model = Company
        fields = ['id', 'name', 'email', 'phone', 'address', 'branches', 'created_at', 'updated_at']
