from django.contrib import admin
from assets.models import Asset, AssetAssignment


@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = ('name', 'asset_type', 'serial_number', 'status', 'company', 'get_current_assignee', 'created_at')
    list_filter = ('status', 'asset_type', 'company', 'created_at')
    search_fields = ('name', 'serial_number', 'company__name')
    readonly_fields = ('id', 'created_at', 'updated_at')
    fieldsets = (
        ('Asset Information', {
            'fields': ('id', 'company', 'name', 'asset_type', 'serial_number', 'status')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def get_current_assignee(self, obj):
        current = obj.assignments.filter(returned_date__isnull=True).first()
        return current.employee if current else "Unassigned"
    get_current_assignee.short_description = 'Current Assignee'


@admin.register(AssetAssignment)
class AssetAssignmentAdmin(admin.ModelAdmin):
    list_display = ('asset', 'employee', 'assigned_date', 'returned_date', 'condition_on_assignment')
    list_filter = ('assigned_date', 'returned_date', 'employee__department')
    search_fields = ('asset__name', 'employee__employee_code', 'employee__first_name', 'employee__last_name')
    readonly_fields = ('id', 'created_at', 'updated_at')
    date_hierarchy = 'assigned_date'
    fieldsets = (
        ('Assignment Information', {
            'fields': ('id', 'asset', 'employee')
        }),
        ('Dates', {
            'fields': ('assigned_date', 'returned_date')
        }),
        ('Condition', {
            'fields': ('condition_on_assignment', 'condition_on_return')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
