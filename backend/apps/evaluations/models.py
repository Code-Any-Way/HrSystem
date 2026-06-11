import uuid
from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from employees.models import Employee

class PerformanceEvaluation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='evaluations')
    evaluator = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='given_evaluations'
    )
    
    # Rating out of 100
    score = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)]
    )
    evaluation_period = models.CharField(max_length=100) # e.g. "Q1 2026", "Annual 2025"
    notes = models.TextField(null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ('employee', 'evaluation_period')

    def __str__(self):
        return f"{self.employee.employee_code} - Score: {self.score} ({self.evaluation_period})"
