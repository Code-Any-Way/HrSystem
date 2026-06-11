from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import User

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('HRMS Settings', {'fields': ('role', 'company', 'branch')}),
    )
    list_display = ('email', 'username', 'role', 'company', 'branch', 'is_staff')
    list_filter = ('role', 'company', 'branch')

admin.site.register(User, CustomUserAdmin)
