from django.contrib import admin
from departments.models import Department

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'created_at')
    list_filter = ('company',)
    search_fields = ('name',)
