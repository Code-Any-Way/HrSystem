from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from accounts.models import Role
from accounts.permissions import IsHRManager
from departments.models import Department
from departments.serializers import DepartmentSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated, IsHRManager]

    def get_queryset(self):
        user = self.request.user
        if user.role == Role.SUPER_ADMIN:
            return Department.objects.all()
        if user.company:
            return Department.objects.filter(company=user.company)
        return Department.objects.none()

    def perform_create(self, serializer):
        user = self.request.user
        if user.role != Role.SUPER_ADMIN:
            serializer.save(company=user.company)
        else:
            serializer.save()
