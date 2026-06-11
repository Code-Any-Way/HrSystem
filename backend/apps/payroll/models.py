import uuid
from django.db import models
from companies.models import Company
from employees.models import Employee

class PayrollRunStatus(models.TextChoices):
    DRAFT = 'DRAFT', 'Draft'
    APPROVED = 'APPROVED', 'Approved'
    PAID = 'PAID', 'Paid'

class PayrollRun(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='payroll_runs')
    month = models.IntegerField()
    year = models.IntegerField()
    status = models.CharField(
        max_length=20, 
        choices=PayrollRunStatus.choices, 
        default=PayrollRunStatus.DRAFT
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('company', 'month', 'year')
        ordering = ['-year', '-month']

    def __str__(self):
        return f"Payroll {self.year}-{self.month} ({self.company.name})"

class PayrollDetail(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    payroll_run = models.ForeignKey(PayrollRun, on_delete=models.CASCADE, related_name='details')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='payroll_details')
    
    # Financial breakdown
    base_salary = models.DecimalField(max_digits=12, decimal_places=2)
    bonus = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    commission = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    overtime = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    
    # Deductions
    absence_deduction = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    late_deduction = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    loan_deduction = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    
    net_salary = models.DecimalField(max_digits=12, decimal_places=2)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('payroll_run', 'employee')

    def save(self, *args, **kwargs):
        # Calculate Net Salary = Base Salary + Bonus + Commission + Overtime - Absence - Late - Loans
        self.net_salary = (
            self.base_salary + 
            self.bonus + 
            self.commission + 
            self.overtime - 
            self.absence_deduction - 
            self.late_deduction - 
            self.loan_deduction
        )
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.employee.employee_code} - Net: {self.net_salary}"
