from django.contrib import admin
from attendance.models import Attendance


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('employee', 'date', 'status', 'check_in', 'check_out', 'ip_address')
    list_filter = ('status', 'date', 'employee__department', 'employee__branch')
    search_fields = ('employee__employee_code', 'employee__first_name', 'employee__last_name', 'ip_address')
    readonly_fields = ('id', 'created_at', 'updated_at')
    date_hierarchy = 'date'
    fieldsets = (
        ('Attendance Information', {
            'fields': ('id', 'employee', 'date', 'status')
        }),
        ('Check In/Out', {
            'fields': ('check_in', 'check_out')
        }),
        ('GPS Data', {
            'fields': ('gps_lat_in', 'gps_lng_in', 'gps_lat_out', 'gps_lng_out'),
            'classes': ('collapse',)
        }),
        ('Additional Info', {
            'fields': ('qr_token', 'ip_address'),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
