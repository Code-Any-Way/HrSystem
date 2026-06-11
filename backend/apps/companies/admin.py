from django.contrib import admin
from companies.models import Company, Branch


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'get_branch_count', 'get_department_count', 'created_at')
    search_fields = ('name', 'email', 'phone', 'address')
    readonly_fields = ('id', 'created_at', 'updated_at', 'get_branch_count', 'get_department_count')
    fieldsets = (
        ('Company Information', {
            'fields': ('id', 'name', 'email', 'phone', 'address')
        }),
        ('Statistics', {
            'fields': ('get_branch_count', 'get_department_count'),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def get_branch_count(self, obj):
        return obj.branches.count()
    get_branch_count.short_description = 'Number of Branches'
    
    def get_department_count(self, obj):
        return obj.departments.count()
    get_department_count.short_description = 'Number of Departments'


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'email', 'phone', 'get_employee_count', 'created_at')
    list_filter = ('company', 'created_at')
    search_fields = ('name', 'email', 'phone', 'address', 'company__name')
    readonly_fields = ('id', 'created_at', 'updated_at', 'get_employee_count')
    fieldsets = (
        ('Branch Information', {
            'fields': ('id', 'company', 'name', 'email', 'phone', 'address')
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
        return obj.users.count()
    get_employee_count.short_description = 'Number of Employees'
