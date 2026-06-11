from rest_framework import viewsets, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from django.db import models
from django_filters.rest_framework import DjangoFilterBackend

from accounts.models import Role
from accounts.permissions import IsHRManager, IsManager
from employees.models import Employee
from expenses.models import ExpenseRequest, ExpenseStatus
from expenses.serializers import ExpenseRequestSerializer

class ExpenseRequestViewSet(viewsets.ModelViewSet):
    serializer_class = ExpenseRequestSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['status', 'category', 'employee']
    ordering_fields = ['created_at', 'amount']

    def get_queryset(self):
        user = self.request.user
        if user.role == Role.SUPER_ADMIN:
            return ExpenseRequest.objects.all()
        # HR/Admins view all company expenses
        if user.role in [Role.COMPANY_ADMIN, Role.HR_MANAGER]:
            return ExpenseRequest.objects.filter(employee__branch__company=user.company)
        # Managers view team requests + their own
        if user.role == Role.MANAGER:
            return ExpenseRequest.objects.filter(
                models.Q(employee__manager=user) | models.Q(employee__user=user)
            )
        # Employees view their own requests
        return ExpenseRequest.objects.filter(employee__user=user)

    def perform_create(self, serializer):
        try:
            employee = Employee.objects.get(user=self.request.user)
            serializer.save(employee=employee)
        except Employee.DoesNotExist:
            # HR creating on behalf
            serializer.save()

    @action(detail=True, methods=['post'], url_path='approve-manager', permission_classes=[IsAuthenticated, IsManager])
    def approve_manager(self, request, pk=None):
        expense = self.get_object()

        # Manager authority checks
        if request.user.role not in [Role.SUPER_ADMIN, Role.COMPANY_ADMIN, Role.HR_MANAGER]:
            if expense.employee.manager != request.user:
                return Response(
                    {"detail": "You are not authorized to approve this request as Manager."},
                    status=status.HTTP_403_FORBIDDEN
                )

        if expense.status != ExpenseStatus.PENDING_MANAGER:
            return Response(
                {"detail": "Request is not in Manager pending status."},
                status=status.HTTP_400_BAD_REQUEST
            )

        expense.status = ExpenseStatus.PENDING_FINANCE
        expense.manager_approved_by = request.user
        expense.manager_approval_date = timezone.now()
        expense.save()

        return Response(ExpenseRequestSerializer(expense).data)

    @action(detail=True, methods=['post'], url_path='approve-finance', permission_classes=[IsAuthenticated, IsHRManager])
    def approve_finance(self, request, pk=None):
        expense = self.get_object()

        if expense.status not in [ExpenseStatus.PENDING_FINANCE, ExpenseStatus.PENDING_MANAGER]:
            return Response(
                {"detail": "Request must be in pending manager or pending finance state."},
                status=status.HTTP_400_BAD_REQUEST
            )

        expense.status = ExpenseStatus.APPROVED
        expense.finance_approved_by = request.user
        expense.finance_approval_date = timezone.now()

        # If manager step was skipped/pre-approved by Finance
        if not expense.manager_approved_by:
            expense.manager_approved_by = request.user
            expense.manager_approval_date = timezone.now()

        expense.save()

        return Response(ExpenseRequestSerializer(expense).data)

    @action(detail=True, methods=['post'], url_path='reject', permission_classes=[IsAuthenticated, IsManager])
    def reject(self, request, pk=None):
        expense = self.get_object()

        # Manager or HR check
        if request.user.role not in [Role.SUPER_ADMIN, Role.COMPANY_ADMIN, Role.HR_MANAGER]:
            if expense.employee.manager != request.user:
                return Response(
                    {"detail": "You are not authorized to reject this request."},
                    status=status.HTTP_403_FORBIDDEN
                )

        if expense.status not in [ExpenseStatus.PENDING_MANAGER, ExpenseStatus.PENDING_FINANCE]:
            return Response(
                {"detail": "Request is not in a pending state to be rejected."},
                status=status.HTTP_400_BAD_REQUEST
            )

        rejection_reason = request.data.get('rejection_reason', 'Rejected by manager/finance')
        expense.status = ExpenseStatus.REJECTED
        expense.rejection_reason = rejection_reason
        expense.save()

        return Response(ExpenseRequestSerializer(expense).data)
