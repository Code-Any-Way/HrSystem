from django.contrib import admin
from expenses.models import ExpenseRequest


@admin.register(ExpenseRequest)
class ExpenseRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'employee', 'category', 'amount', 'status', 'created_at')
    list_filter = ('status', 'category', 'created_at', 'employee__department')
    search_fields = ('title', 'description', 'employee__first_name', 'employee__last_name')
    readonly_fields = ('id', 'created_at', 'updated_at')
    date_hierarchy = 'created_at'
    fieldsets = (
        ('Expense Information', {
            'fields': ('id', 'employee', 'title', 'description', 'category', 'amount')
        }),
        ('Approval Chain', {
            'fields': ('status', 'manager_approved_by', 'manager_approval_date', 'finance_approved_by', 'finance_approval_date', 'rejection_reason')
        }),
        ('Attachments', {
            'fields': ('receipt',),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
