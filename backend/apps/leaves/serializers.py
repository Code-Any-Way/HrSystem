from rest_framework import serializers
from django.utils import timezone
from leaves.models import LeaveRequest, LeaveBalance, LeaveType

class LeaveBalanceSerializer(serializers.ModelSerializer):
    employee_code = serializers.ReadOnlyField(source='employee.employee_code')
    employee_name = serializers.SerializerMethodField()

    class Meta:
        model = LeaveBalance
        fields = [
            'id', 'employee', 'employee_code', 'employee_name', 'year', 
            'annual_total', 'annual_used', 'sick_total', 'sick_used', 
            'emergency_total', 'emergency_used'
        ]

    def get_employee_name(self, obj):
        return f"{obj.employee.first_name} {obj.employee.last_name}"

class LeaveRequestSerializer(serializers.ModelSerializer):
    employee_code = serializers.ReadOnlyField(source='employee.employee_code')
    employee_name = serializers.SerializerMethodField()
    duration_days = serializers.ReadOnlyField()

    class Meta:
        model = LeaveRequest
        fields = [
            'id', 'employee', 'employee_code', 'employee_name', 'leave_type', 
            'start_date', 'end_date', 'reason', 'status', 'duration_days',
            'manager_approved_by', 'manager_approval_date', 'hr_approved_by', 
            'hr_approval_date', 'rejection_reason', 'created_at', 'updated_at'
        ]
        read_only_fields = [
            'id', 'status', 'manager_approved_by', 'manager_approval_date', 
            'hr_approved_by', 'hr_approval_date', 'rejection_reason', 'employee'
        ]

    def get_employee_name(self, obj):
        return f"{obj.employee.first_name} {obj.employee.last_name}"

    def validate(self, attrs):
        start_date = attrs.get('start_date')
        end_date = attrs.get('end_date')
        if start_date > end_date:
            raise serializers.ValidationError("Start date must be before or equal to end date.")
            
        request = self.context.get('request')
        if not request or not request.user.is_authenticated:
            return attrs

        try:
            employee = request.user.employee
        except AttributeError:
            # HR creating leave requests for others is allowed, validation can skip user scope check
            employee = attrs.get('employee')
            if not employee:
                raise serializers.ValidationError("Employee must be specified.")

        # Check balance for non-unpaid leaves
        leave_type = attrs.get('leave_type')
        if leave_type != LeaveType.UNPAID:
            year = start_date.year
            balance, _ = LeaveBalance.objects.get_or_create(
                employee=employee, 
                year=year,
                defaults={
                    'annual_total': 21,
                    'sick_total': 15,
                    'emergency_total': 7
                }
            )
            
            days = (end_date - start_date).days + 1
            if leave_type == LeaveType.ANNUAL:
                avail = balance.annual_total - balance.annual_used
            elif leave_type == LeaveType.SICK:
                avail = balance.sick_total - balance.sick_used
            elif leave_type == LeaveType.EMERGENCY:
                avail = balance.emergency_total - balance.emergency_used
            else:
                avail = 0
                
            if days > avail:
                raise serializers.ValidationError(
                    f"Insufficient leave balance for {leave_type}. "
                    f"Requested {days} days, but only {avail} days left."
                )

        return attrs
