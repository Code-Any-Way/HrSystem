import uuid
from django.db import models
from employees.models import Employee

class AttendanceStatus(models.TextChoices):
    PRESENT = 'PRESENT', 'Present'
    ABSENT = 'ABSENT', 'Absent'
    LATE = 'LATE', 'Late'
    LEAVE = 'LEAVE', 'Leave'
    HOLIDAY = 'HOLIDAY', 'Holiday'

class Attendance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='attendances')
    date = models.DateField()
    check_in = models.DateTimeField(null=True, blank=True)
    check_out = models.DateTimeField(null=True, blank=True)
    status = models.CharField(
        max_length=20, 
        choices=AttendanceStatus.choices, 
        default=AttendanceStatus.PRESENT
    )
    
    # QR token verification
    qr_token = models.CharField(max_length=255, null=True, blank=True)
    
    # GPS details (Latitude & Longitude)
    gps_lat_in = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    gps_lng_in = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    gps_lat_out = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    gps_lng_out = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date', '-check_in']
        unique_together = ('employee', 'date')

    def __str__(self):
        return f"{self.employee.employee_code} - {self.date} ({self.status})"
