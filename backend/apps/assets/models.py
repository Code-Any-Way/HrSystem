import uuid
from django.db import models
from companies.models import Company
from employees.models import Employee

class AssetType(models.TextChoices):
    LAPTOP = 'LAPTOP', 'Laptop'
    PHONE = 'PHONE', 'Phone'
    SIM_CARD = 'SIM_CARD', 'SIM Card'
    VEHICLE = 'VEHICLE', 'Vehicle'
    OTHER = 'OTHER', 'Other'

class AssetStatus(models.TextChoices):
    AVAILABLE = 'AVAILABLE', 'Available'
    ASSIGNED = 'ASSIGNED', 'Assigned'
    REPAIR = 'REPAIR', 'Under Repair'
    RETIRED = 'RETIRED', 'Retired'

class Asset(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='assets')
    name = models.CharField(max_length=255)
    asset_type = models.CharField(max_length=50, choices=AssetType.choices, default=AssetType.LAPTOP)
    serial_number = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=20, choices=AssetStatus.choices, default=AssetStatus.AVAILABLE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name} ({self.serial_number}) - {self.status}"

class AssetAssignment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE, related_name='assignments')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='assigned_assets')
    assigned_date = models.DateField()
    returned_date = models.DateField(null=True, blank=True)
    condition_on_assignment = models.TextField(null=True, blank=True)
    condition_on_return = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-assigned_date']

    def __str__(self):
        return f"{self.asset.name} assigned to {self.employee.employee_code}"
