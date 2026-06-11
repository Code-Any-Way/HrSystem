from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from accounts.models import Role
from accounts.permissions import IsCompanyAdmin
from companies.models import Company, Branch
from companies.serializers import CompanySerializer, BranchSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated, IsCompanyAdmin]

    def get_queryset(self):
        user = self.request.user
        if user.role == Role.SUPER_ADMIN:
            return Company.objects.all()
        # Non-superadmins only access their own company
        if user.company:
            return Company.objects.filter(id=user.company.id)
        return Company.objects.none()

class BranchViewSet(viewsets.ModelViewSet):
    serializer_class = BranchSerializer
    permission_classes = [IsAuthenticated, IsCompanyAdmin]

    def get_queryset(self):
        user = self.request.user
        if user.role == Role.SUPER_ADMIN:
            return Branch.objects.all()
        if user.company:
            return Branch.objects.filter(company=user.company)
        return Branch.objects.none()

    def perform_create(self, serializer):
        # Enforce that non-superadmins can only create branches for their own company
        user = self.request.user
        if user.role != Role.SUPER_ADMIN:
            serializer.save(company=user.company)
        else:
            serializer.save()
