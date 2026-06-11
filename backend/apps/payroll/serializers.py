from rest_framework import serializers
from payroll.models import PayrollRun, PayrollDetail
from employees.serializers import EmployeeMiniSerializer

class PayrollDetailSerializer(serializers.ModelSerializer):
    employee_details = EmployeeMiniSerializer(source='employee', read_only=True)
    employee_code = serializers.ReadOnlyField(source='employee.employee_code')
    employee_name = serializers.SerializerMethodField()

    class Meta:
        model = PayrollDetail
        fields = [
            'id', 'payroll_run', 'employee', 'employee_code', 'employee_name', 
            'employee_details', 'base_salary', 'bonus', 'commission', 'overtime', 
            'absence_deduction', 'late_deduction', 'loan_deduction', 'net_salary', 
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'net_salary']

    def get_employee_name(self, obj):
        return f"{obj.employee.first_name} {obj.employee.last_name}"

class PayrollRunSerializer(serializers.ModelSerializer):
    details_count = serializers.SerializerMethodField()
    total_net_salary = serializers.SerializerMethodField()

    class Meta:
        model = PayrollRun
        fields = ['id', 'company', 'month', 'year', 'status', 'details_count', 'total_net_salary', 'created_at', 'updated_at']
        read_only_fields = ['id', 'company', 'status']

    def get_details_count(self, obj):
        return obj.details.count()

    def get_total_net_salary(self, obj):
        return sum(detail.net_salary for detail in obj.details.all())

class PayrollGenerateSerializer(serializers.Serializer):
    month = serializers.IntegerField(min_value=1, max_value=12)
    year = serializers.IntegerField(min_value=2000, max_value=2100)
