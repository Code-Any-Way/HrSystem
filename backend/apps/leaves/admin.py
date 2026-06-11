from django.contrib import admin
from leaves.models import LeaveRequest


@admin.register(LeaveRequest)
class LeaveRequestAdmin(admin.ModelAdmin):
    list_display = ('employee', 'leave_type', 'start_date', 'end_date', 'status', 'get_duration')
    list_filter = ('status', 'leave_type', 'start_date', 'employee__department')
    search_fields = ('employee__employee_code', 'employee__first_name', 'employee__last_name', 'reason')
    readonly_fields = ('id', 'created_at', 'updated_at')
    date_hierarchy = 'start_date'
    
    fieldsets = (
        ('Leave Request Information', {
            'fields': ('id', 'employee', 'leave_type', 'reason')
        }),
        ('Dates', {
            'fields': ('start_date', 'end_date')
        }),
        ('Status & Approvals', {
            'fields': ('status', 'manager_approved_by', 'manager_approval_date', 'hr_approved_by', 'hr_approval_date', 'rejection_reason')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def get_duration(self, obj):
        """Display leave duration in days"""
        if obj.start_date and obj.end_date:
            duration = (obj.end_date - obj.start_date).days + 1
            return f"{duration} days"
        return "-"
    get_duration.short_description = 'Duration'
