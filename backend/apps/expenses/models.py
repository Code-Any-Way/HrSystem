import uuid
from django.db import models
from django.conf import settings
from employees.models import Employee

class ExpenseStatus(models.TextChoices):
    PENDING_MANAGER = 'PENDING_MANAGER', 'Pending Manager Approval'
    PENDING_FINANCE = 'PENDING_FINANCE', 'Pending Finance Approval'
    APPROVED = 'APPROVED', 'Approved'
    REJECTED = 'REJECTED', 'Rejected'

class ExpenseCategory(models.TextChoices):
    TRAVEL = 'TRAVEL', 'Travel'
    MEALS = 'MEALS', 'Meals'
    SUPPLIES = 'SUPPLIES', 'Office Supplies'
    UTILITIES = 'UTILITIES', 'Utilities'
    OTHER = 'OTHER', 'Other'

class ExpenseRequest(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='expenses')
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(
        max_length=50, 
        choices=ExpenseCategory.choices, 
        default=ExpenseCategory.OTHER
    )
    receipt = models.FileField(upload_to='receipts/', null=True, blank=True)
    status = models.CharField(
        max_length=20, 
        choices=ExpenseStatus.choices, 
        default=ExpenseStatus.PENDING_MANAGER
    )
    
    # Approval chain
    manager_approved_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='manager_approved_expenses'
    )
    manager_approval_date = models.DateTimeField(null=True, blank=True)
    
    finance_approved_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='finance_approved_expenses'
    )
    finance_approval_date = models.DateTimeField(null=True, blank=True)
    
    rejection_reason = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} (${self.amount}) - {self.status}"
