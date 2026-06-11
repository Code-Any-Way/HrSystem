from django.contrib import admin
from employees.models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_code', 'first_name', 'last_name', 'email', 'job_title', 'department', 'status', 'employment_type', 'hire_date')
    list_filter = ('status', 'employment_type', 'department', 'branch', 'team', 'hire_date', 'created_at')
    search_fields = ('employee_code', 'first_name', 'last_name', 'email', 'user__email')
    readonly_fields = ('id', 'created_at', 'updated_at')
    date_hierarchy = 'hire_date'
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('id', 'user', 'first_name', 'last_name', 'email', 'phone', 'date_of_birth', 'gender', 'national_id', 'address')
        }),
        ('Employment Details', {
            'fields': ('employee_code', 'job_title', 'department', 'team', 'branch', 'manager', 'employment_type', 'status')
        }),
        ('Contract', {
            'fields': ('hire_date', 'base_salary'),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
