from django.contrib import admin
from payroll.models import PayrollRun, PayrollDetail


@admin.register(PayrollRun)
class PayrollRunAdmin(admin.ModelAdmin):
    list_display = ('company', 'year', 'month', 'status', 'get_employee_count', 'created_at')
    list_filter = ('status', 'year', 'month', 'company', 'created_at')
    search_fields = ('company__name',)
    readonly_fields = ('id', 'created_at', 'updated_at', 'get_employee_count')
    date_hierarchy = 'created_at'
    fieldsets = (
        ('Payroll Run Information', {
            'fields': ('id', 'company', 'month', 'year', 'status')
        }),
        ('Statistics', {
            'fields': ('get_employee_count',),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def get_employee_count(self, obj):
        return obj.details.count()
    get_employee_count.short_description = 'Number of Employees'


@admin.register(PayrollDetail)
class PayrollDetailAdmin(admin.ModelAdmin):
    list_display = ('employee', 'payroll_run', 'base_salary', 'net_salary', 'created_at')
    list_filter = ('payroll_run', 'payroll_run__status', 'employee__department')
    search_fields = ('employee__employee_code', 'employee__first_name', 'employee__last_name')
    readonly_fields = ('id', 'created_at', 'updated_at', 'net_salary')
    date_hierarchy = 'created_at'
    fieldsets = (
        ('Payroll Information', {
            'fields': ('id', 'payroll_run', 'employee')
        }),
        ('Salary Components', {
            'fields': ('base_salary', 'bonus', 'commission', 'overtime')
        }),
        ('Deductions', {
            'fields': ('absence_deduction', 'late_deduction', 'loan_deduction')
        }),
        ('Net Salary', {
            'fields': ('net_salary',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
