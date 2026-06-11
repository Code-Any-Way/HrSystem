from django.contrib import admin
from notifications.models import Notification


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'notification_type', 'is_read', 'title', 'created_at')
    list_filter = ('notification_type', 'is_read', 'created_at', 'user__role')
    search_fields = ('user__first_name', 'user__last_name', 'title', 'message')
    readonly_fields = ('id', 'created_at')
    date_hierarchy = 'created_at'
    fieldsets = (
        ('Notification Information', {
            'fields': ('id', 'user', 'notification_type', 'title')
        }),
        ('Content', {
            'fields': ('message',)
        }),
        ('Status', {
            'fields': ('is_read',)
        }),
        ('Timestamp', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
    
    def has_add_permission(self, request):
        """Notifications are auto-created, don't allow manual addition"""
        return False
