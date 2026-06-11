from rest_framework import viewsets, status, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from django.db import transaction, models
from accounts.models import Role
from accounts.permissions import IsHRManager
from assets.models import Asset, AssetAssignment, AssetStatus
from assets.serializers import AssetSerializer, AssetAssignmentSerializer

class AssetViewSet(viewsets.ModelViewSet):
    serializer_class = AssetSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['asset_type', 'status']
    search_fields = ['name', 'serial_number']

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [IsAuthenticated()]
        return [IsAuthenticated(), IsHRManager()]

    def get_queryset(self):
        user = self.request.user
        if user.role == Role.SUPER_ADMIN:
            return Asset.objects.all()
        if user.company:
            return Asset.objects.filter(company=user.company)
        return Asset.objects.none()

    def perform_create(self, serializer):
        user = self.request.user
        if user.role != Role.SUPER_ADMIN:
            serializer.save(company=user.company)
        else:
            serializer.save()

class AssetAssignmentViewSet(viewsets.ModelViewSet):
    serializer_class = AssetAssignmentSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['asset', 'employee']

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [IsAuthenticated()]
        return [IsAuthenticated(), IsHRManager()]

    def get_queryset(self):
        user = self.request.user
        if user.role == Role.SUPER_ADMIN:
            return AssetAssignment.objects.all()
        if user.role in [Role.COMPANY_ADMIN, Role.HR_MANAGER]:
            return AssetAssignment.objects.filter(asset__company=user.company)
        # Employees see their own assigned assets
        return AssetAssignment.objects.filter(employee__user=user)

    @transaction.atomic
    def perform_create(self, serializer):
        assignment = serializer.save()
        # Mark asset as assigned
        asset = assignment.asset
        asset.status = AssetStatus.ASSIGNED
        asset.save()

    @transaction.atomic
    def perform_update(self, serializer):
        assignment = serializer.save()
        # If returned, release the asset back to available status
        if assignment.returned_date:
            asset = assignment.asset
            asset.status = AssetStatus.AVAILABLE
            asset.save()
