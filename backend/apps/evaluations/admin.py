from django.contrib import admin
from evaluations.models import PerformanceEvaluation


@admin.register(PerformanceEvaluation)
class PerformanceEvaluationAdmin(admin.ModelAdmin):
    list_display = ('employee', 'evaluator', 'evaluation_period', 'score', 'created_at')
    list_filter = ('score', 'evaluation_period', 'created_at', 'employee__department')
    search_fields = ('employee__first_name', 'employee__last_name', 'employee__employee_code', 'evaluator__first_name', 'evaluator__last_name')
    readonly_fields = ('id', 'created_at', 'updated_at')
    date_hierarchy = 'created_at'
    fieldsets = (
        ('Evaluation Information', {
            'fields': ('id', 'employee', 'evaluator', 'evaluation_period')
        }),
        ('Score & Notes', {
            'fields': ('score', 'notes')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
