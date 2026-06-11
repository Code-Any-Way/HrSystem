from rest_framework.permissions import BasePermission
from accounts.models import Role

class IsSuperAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == Role.SUPER_ADMIN

class IsCompanyAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in [Role.SUPER_ADMIN, Role.COMPANY_ADMIN]

class IsHRManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in [Role.SUPER_ADMIN, Role.COMPANY_ADMIN, Role.HR_MANAGER]

class IsManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in [Role.SUPER_ADMIN, Role.COMPANY_ADMIN, Role.HR_MANAGER, Role.MANAGER]

class IsEmployee(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

class IsOwnerOrAdmin(BasePermission):
    """
    Custom permission to only allow owners of an object to edit or read it,
    or allow HR/Company admins to access it.
    """
    def has_object_permission(self, request, view, obj):
        if request.user.role in [Role.SUPER_ADMIN, Role.COMPANY_ADMIN, Role.HR_MANAGER]:
            return True
        # Check if the object is owned by the user
        if hasattr(obj, 'user'):
            return obj.user == request.user
        if hasattr(obj, 'employee'):
            return obj.employee.user == request.user
        return False
