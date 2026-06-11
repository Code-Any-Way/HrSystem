from rest_framework import serializers
from expenses.models import ExpenseRequest

class ExpenseRequestSerializer(serializers.ModelSerializer):
    employee_code = serializers.ReadOnlyField(source='employee.employee_code')
    employee_name = serializers.SerializerMethodField()

    class Meta:
        model = ExpenseRequest
        fields = [
            'id', 'employee', 'employee_code', 'employee_name', 'title', 
            'description', 'amount', 'category', 'receipt', 'status', 
            'manager_approved_by', 'manager_approval_date', 'finance_approved_by', 
            'finance_approval_date', 'rejection_reason', 'created_at', 'updated_at'
        ]
        read_only_fields = [
            'id', 'status', 'manager_approved_by', 'manager_approval_date', 
            'finance_approved_by', 'finance_approval_date', 'rejection_reason', 'employee'
        ]

    def get_employee_name(self, obj):
        return f"{obj.employee.first_name} {obj.employee.last_name}"
