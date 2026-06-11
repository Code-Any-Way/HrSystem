from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from accounts.models import Role
from accounts.permissions import IsHRManager
from audit_logs.models import AuditLog
from audit_logs.serializers import AuditLogSerializer

class AuditLogViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    Viewset to read audit logs. Operations (Create, Update, Delete) are blocked, 
    since audit logs are only generated via model signals.
    """
    serializer_class = AuditLogSerializer
    permission_classes = [IsAuthenticated, IsHRManager]

    def get_queryset(self):
        user = self.request.user
        if user.role == Role.SUPER_ADMIN:
            return AuditLog.objects.all()
        # Non-superadmins see logs of actions committed by their company users
        if user.company:
            return AuditLog.objects.filter(user__company=user.company)
        return AuditLog.objects.none()
