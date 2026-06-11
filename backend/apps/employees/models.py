import uuid
from django.db import models
from django.conf import settings
from companies.models import Branch
from departments.models import Department
from teams.models import Team

class EmploymentStatus(models.TextChoices):
    ACTIVE = 'ACTIVE', 'Active'
    INACTIVE = 'INACTIVE', 'Inactive'
    TERMINATED = 'TERMINATED', 'Terminated'
    SUSPENDED = 'SUSPENDED', 'Suspended'

class EmploymentType(models.TextChoices):
    FULL_TIME = 'FULL_TIME', 'Full Time'
    PART_TIME = 'PART_TIME', 'Part Time'
    CONTRACT = 'CONTRACT', 'Contract'
    INTERNSHIP = 'INTERNSHIP', 'Internship'

class GenderChoices(models.TextChoices):
    MALE = 'MALE', 'Male'
    FEMALE = 'FEMALE', 'Female'
    OTHER = 'OTHER', 'Other'

class Employee(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # One-to-one link to auth user
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='employee'
    )
    employee_code = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    national_id = models.CharField(max_length=100, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GenderChoices.choices, default=GenderChoices.OTHER)
    
    # Position & Org details
    job_title = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.PROTECT, related_name='employees')
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True, related_name='employees')
    branch = models.ForeignKey(Branch, on_delete=models.PROTECT, related_name='employees')
    
    # Manager can be any User (normally role = MANAGER or HR_MANAGER)
    manager = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='managed_employees'
    )
    
    # Contract details
    employment_type = models.CharField(
        max_length=20, 
        choices=EmploymentType.choices, 
        default=EmploymentType.FULL_TIME
    )
    status = models.CharField(
        max_length=20, 
        choices=EmploymentStatus.choices, 
        default=EmploymentStatus.ACTIVE
    )
    hire_date = models.DateField()
    base_salary = models.DecimalField(max_digits=12, decimal_places=2)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['employee_code']

    def __str__(self):
        return f"{self.employee_code} - {self.first_name} {self.last_name}"
