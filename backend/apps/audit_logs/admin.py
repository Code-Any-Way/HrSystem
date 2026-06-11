from django.contrib import admin
from audit_logs.models import AuditLog


@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'action', 'model_name', 'created_at', 'ip_address')
    list_filter = ('action', 'created_at', 'model_name')
    search_fields = ('user__first_name', 'user__last_name', 'user__email', 'model_name', 'ip_address', 'object_id')
    readonly_fields = ('id', 'user', 'action', 'model_name', 'object_id', 'old_data', 'new_data', 'ip_address', 'created_at')
    date_hierarchy = 'created_at'
    fieldsets = (
        ('Audit Information', {
            'fields': ('id', 'user', 'action', 'model_name', 'object_id', 'created_at')
        }),
        ('Changes', {
            'fields': ('old_data', 'new_data'),
            'classes': ('collapse',)
        }),
        ('System Information', {
            'fields': ('ip_address',),
            'classes': ('collapse',)
        }),
    )
    
    def has_add_permission(self, request):
        """Audit logs are auto-created, don't allow manual addition"""
        return False
    
    def has_delete_permission(self, request, obj=None):
        """Prevent deletion of audit logs"""
        return False
