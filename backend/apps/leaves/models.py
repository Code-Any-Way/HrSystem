import uuid
from django.db import models
from django.conf import settings
from employees.models import Employee

class LeaveType(models.TextChoices):
    ANNUAL = 'ANNUAL', 'Annual'
    SICK = 'SICK', 'Sick'
    EMERGENCY = 'EMERGENCY', 'Emergency'
    UNPAID = 'UNPAID', 'Unpaid'

class LeaveStatus(models.TextChoices):
    PENDING_MANAGER = 'PENDING_MANAGER', 'Pending Manager Approval'
    PENDING_HR = 'PENDING_HR', 'Pending HR Approval'
    APPROVED = 'APPROVED', 'Approved'
    REJECTED = 'REJECTED', 'Rejected'

class LeaveRequest(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='leave_requests')
    leave_type = models.CharField(max_length=20, choices=LeaveType.choices, default=LeaveType.ANNUAL)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(
        max_length=20, 
        choices=LeaveStatus.choices, 
        default=LeaveStatus.PENDING_MANAGER
    )
    
    # Workflow triggers
    manager_approved_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='manager_approved_leaves'
    )
    manager_approval_date = models.DateTimeField(null=True, blank=True)
    
    hr_approved_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='hr_approved_leaves'
    )
    hr_approval_date = models.DateTimeField(null=True, blank=True)
    
    rejection_reason = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    @property
    def duration_days(self):
        return (self.end_date - self.start_date).days + 1

    def __str__(self):
        return f"{self.employee.employee_code} - {self.leave_type} ({self.status})"

class LeaveBalance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='leave_balances')
    year = models.IntegerField()
    
    # Balances
    annual_total = models.IntegerField(default=21)
    annual_used = models.IntegerField(default=0)
    
    sick_total = models.IntegerField(default=15)
    sick_used = models.IntegerField(default=0)
    
    emergency_total = models.IntegerField(default=7)
    emergency_used = models.IntegerField(default=0)
    
    class Meta:
        unique_together = ('employee', 'year')

    def __str__(self):
        return f"{self.employee.employee_code} - Year {self.year}"
