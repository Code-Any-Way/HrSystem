from django.contrib import admin
from employees.models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_code', 'first_name', 'last_name', 'email', 'job_title', 'department', 'status')
    list_filter = ('status', 'employment_type', 'department', 'branch')
    search_fields = ('employee_code', 'first_name', 'last_name', 'email')

admin.site.register(Employee, EmployeeAdmin)
