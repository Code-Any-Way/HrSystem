from django.contrib import admin
from companies.models import Company, Branch

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at')
    search_fields = ('name', 'email')

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'email', 'phone', 'created_at')
    list_filter = ('company',)
    search_fields = ('name', 'email')
