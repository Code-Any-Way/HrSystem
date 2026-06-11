from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import Group, Permission
from accounts.models import User


class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('HRMS Settings', {'fields': ('role', 'company', 'branch')}),
    )
    list_display = ('email', 'username', 'role', 'company', 'branch', 'is_staff', 'is_superuser', 'is_active')
    list_filter = ('role', 'company', 'branch', 'is_staff', 'is_superuser', 'is_active')
    search_fields = ('email', 'username', 'first_name', 'last_name')
    filter_horizontal = ('groups', 'user_permissions')


class CustomGroupAdmin(GroupAdmin):
    list_display = ('name', 'permission_count')
    filter_horizontal = ('permissions',)
    
    def permission_count(self, obj):
        return obj.permissions.count()
    permission_count.short_description = 'Number of Permissions'


class PermissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'codename', 'content_type')
    list_filter = ('content_type',)
    search_fields = ('name', 'codename')
    readonly_fields = ('id',)


admin.site.register(User, CustomUserAdmin)
admin.site.unregister(Group)
admin.site.register(Group, CustomGroupAdmin)
admin.site.register(Permission, PermissionAdmin)
