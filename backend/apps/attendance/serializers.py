from rest_framework import serializers
from attendance.models import Attendance

class AttendanceSerializer(serializers.ModelSerializer):
    employee_code = serializers.ReadOnlyField(source='employee.employee_code')
    employee_name = serializers.SerializerMethodField()

    class Meta:
        model = Attendance
        fields = [
            'id', 'employee', 'employee_code', 'employee_name', 'date', 
            'check_in', 'check_out', 'status', 'qr_token', 
            'gps_lat_in', 'gps_lng_in', 'gps_lat_out', 'gps_lng_out', 
            'ip_address', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'date', 'check_in', 'check_out', 'status', 'employee']

    def get_employee_name(self, obj):
        return f"{obj.employee.first_name} {obj.employee.last_name}"

class CheckInSerializer(serializers.Serializer):
    gps_lat = serializers.DecimalField(max_digits=9, decimal_places=6, required=False)
    gps_lng = serializers.DecimalField(max_digits=9, decimal_places=6, required=False)
    qr_token = serializers.CharField(max_length=255, required=False)

class CheckOutSerializer(serializers.Serializer):
    gps_lat = serializers.DecimalField(max_digits=9, decimal_places=6, required=False)
    gps_lng = serializers.DecimalField(max_digits=9, decimal_places=6, required=False)
