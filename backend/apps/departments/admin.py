from django.contrib import admin
from departments.models import Department


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'created_at', 'updated_at')
    list_filter = ('company', 'created_at')
    search_fields = ('name', 'description', 'company__name')
    readonly_fields = ('id', 'created_at', 'updated_at')
    fieldsets = (
        ('Department Information', {
            'fields': ('id', 'company', 'name', 'description')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
