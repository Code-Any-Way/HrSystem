from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.db import transaction
from employees.models import Employee
from accounts.models import Role

class EmployeeSerializer(serializers.ModelSerializer):
    company_name = serializers.ReadOnlyField(source='branch.company.name')
    branch_name = serializers.ReadOnlyField(source='branch.name')
    department_name = serializers.ReadOnlyField(source='department.name')
    team_name = serializers.ReadOnlyField(source='team.name')
    manager_name = serializers.SerializerMethodField()
    role = serializers.CharField(write_only=True, required=False, default=Role.EMPLOYEE)

    class Meta:
        model = Employee
        fields = [
            'id', 'employee_code', 'first_name', 'last_name', 'email', 'phone', 
            'address', 'national_id', 'date_of_birth', 'gender', 'job_title', 
            'department', 'department_name', 'team', 'team_name', 'branch', 
            'branch_name', 'company_name', 'manager', 'manager_name', 
            'employment_type', 'status', 'hire_date', 'base_salary', 'role'
        ]

    def get_manager_name(self, obj):
        if obj.manager:
            return f"{obj.manager.first_name} {obj.manager.last_name}".strip() or obj.manager.email
        return None

    @transaction.atomic
    def create(self, validated_data):
        email = validated_data.get('email')
        first_name = validated_data.get('first_name')
        last_name = validated_data.get('last_name')
        branch = validated_data.get('branch')
        role = validated_data.pop('role', Role.EMPLOYEE)
        
        User = get_user_model()
        
        # Build user
        user, created = User.objects.get_or_create(
            email=email,
            defaults={
                'username': email,
                'first_name': first_name,
                'last_name': last_name,
                'role': role,
                'company': branch.company if branch else None,
                'branch': branch
            }
        )
        if created:
            # Set a default password based on employee_code
            pwd = validated_data.get('employee_code', 'Welcome@HRMS123')
            user.set_password(pwd)
            user.save()
            
        validated_data['user'] = user
        employee = Employee.objects.create(**validated_data)
        return employee

    @transaction.atomic
    def update(self, instance, validated_data):
        user = instance.user
        user_changed = False
        
        if 'email' in validated_data:
            user.email = validated_data['email']
            user.username = validated_data['email']
            user_changed = True
        if 'first_name' in validated_data:
            user.first_name = validated_data['first_name']
            user_changed = True
        if 'last_name' in validated_data:
            user.last_name = validated_data['last_name']
            user_changed = True
        if 'branch' in validated_data:
            user.branch = validated_data['branch']
            user.company = validated_data['branch'].company if validated_data['branch'] else None
            user_changed = True
            
        if user_changed:
            user.save()
            
        return super().update(instance, validated_data)
class EmployeeMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'employee_code', 'first_name', 'last_name', 'job_title', 'email']
