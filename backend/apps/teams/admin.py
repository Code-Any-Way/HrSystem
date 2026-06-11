from django.contrib import admin
from teams.models import Team


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'leader', 'created_at', 'updated_at')
    list_filter = ('department', 'department__company', 'created_at')
    search_fields = ('name', 'department__name', 'leader__first_name', 'leader__last_name')
    readonly_fields = ('id', 'created_at', 'updated_at')
    fieldsets = (
        ('Team Information', {
            'fields': ('id', 'department', 'name', 'leader')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
