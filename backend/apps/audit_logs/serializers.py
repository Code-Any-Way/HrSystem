from rest_framework import serializers
from audit_logs.models import AuditLog

class AuditLogSerializer(serializers.ModelSerializer):
    user_email = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = AuditLog
        fields = ['id', 'user', 'user_email', 'action', 'model_name', 'object_id', 'old_data', 'new_data', 'ip_address', 'created_at']
