import uuid
from django.db import models
from django.conf import settings

class AuditLog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='audit_logs'
    )
    action = models.CharField(max_length=50) # e.g. "CREATE", "UPDATE", "DELETE", "LOGIN", "LOGOUT"
    model_name = models.CharField(max_length=100) # e.g. "Employee", "LeaveRequest"
    object_id = models.CharField(max_length=255)
    old_data = models.JSONField(null=True, blank=True)
    new_data = models.JSONField(null=True, blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        user_str = self.user.email if self.user else "Anonymous"
        return f"{user_str} - {self.action} {self.model_name} ({self.created_at})"
