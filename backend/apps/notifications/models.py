import uuid
from django.db import models
from django.conf import settings

class NotificationType(models.TextChoices):
    INFO = 'INFO', 'Information'
    WARNING = 'WARNING', 'Warning'
    SUCCESS = 'SUCCESS', 'Success'
    DANGER = 'DANGER', 'Danger'

class Notification(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='notifications'
    )
    notification_type = models.CharField(
        max_length=20, 
        choices=NotificationType.choices, 
        default=NotificationType.INFO
    )
    title = models.CharField(max_length=255)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} for {self.user.email} - Read: {self.is_read}"
