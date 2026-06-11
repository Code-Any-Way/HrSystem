from rest_framework import viewsets, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from django.db import transaction, models
from django_filters.rest_framework import DjangoFilterBackend
from accounts.models import Role
from accounts.permissions import IsHRManager, IsManager
from employees.models import Employee
from leaves.models import LeaveRequest, LeaveBalance, LeaveStatus, LeaveType
from leaves.serializers import LeaveRequestSerializer, LeaveBalanceSerializer

class LeaveRequestViewSet(viewsets.ModelViewSet):
    serializer_class = LeaveRequestSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['status', 'leave_type', 'employee']
    ordering_fields = ['created_at', 'start_date']

    def get_queryset(self):
        user = self.request.user
        if user.role == Role.SUPER_ADMIN:
            return LeaveRequest.objects.all()
        # HR and Company Admins see their company's leave requests
        if user.role in [Role.COMPANY_ADMIN, Role.HR_MANAGER]:
            return LeaveRequest.objects.filter(employee__branch__company=user.company)
        # Managers view their team members' requests + their own
        if user.role == Role.MANAGER:
            return LeaveRequest.objects.filter(
                models.Q(employee__manager=user) | models.Q(employee__user=user)
            )
        # Employees view their own requests
        return LeaveRequest.objects.filter(employee__user=user)

    def perform_create(self, serializer):
        try:
            employee = Employee.objects.get(user=self.request.user)
            serializer.save(employee=employee)
        except Employee.DoesNotExist:
            # HR creating leave on behalf of an employee
            serializer.save()

    @action(detail=True, methods=['post'], url_path='approve-manager', permission_classes=[IsAuthenticated, IsManager])
    def approve_manager(self, request, pk=None):
        leave_request = self.get_object()
        
        # Verify permissions: must be the employee's manager
        if request.user.role not in [Role.SUPER_ADMIN, Role.COMPANY_ADMIN, Role.HR_MANAGER]:
            if leave_request.employee.manager != request.user:
                return Response(
                    {"detail": "You are not authorized to approve this request as Manager."},
                    status=status.HTTP_403_FORBIDDEN
                )

        if leave_request.status != LeaveStatus.PENDING_MANAGER:
            return Response(
                {"detail": "Leave request is not in Manager pending status."},
                status=status.HTTP_400_BAD_REQUEST
            )

        leave_request.status = LeaveStatus.PENDING_HR
        leave_request.manager_approved_by = request.user
        leave_request.manager_approval_date = timezone.now()
        leave_request.save()

        return Response(LeaveRequestSerializer(leave_request).data)

    @action(detail=True, methods=['post'], url_path='approve-hr', permission_classes=[IsAuthenticated, IsHRManager])
    @transaction.atomic
    def approve_hr(self, request, pk=None):
        leave_request = self.get_object()

        if leave_request.status not in [LeaveStatus.PENDING_HR, LeaveStatus.PENDING_MANAGER]:
            return Response(
                {"detail": "Leave request is not in a pending state."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Deduct days from leave balance
        days = leave_request.duration_days
        year = leave_request.start_date.year
        employee = leave_request.employee

        if leave_request.leave_type != LeaveType.UNPAID:
            balance, _ = LeaveBalance.objects.get_or_create(
                employee=employee,
                year=year,
                defaults={
                    'annual_total': 21,
                    'sick_total': 15,
                    'emergency_total': 7
                }
            )

            # Check and update
            if leave_request.leave_type == LeaveType.ANNUAL:
                if balance.annual_used + days > balance.annual_total:
                    return Response({"detail": "Insufficient Annual leave balance."}, status=status.HTTP_400_BAD_REQUEST)
                balance.annual_used += days
            elif leave_request.leave_type == LeaveType.SICK:
                if balance.sick_used + days > balance.sick_total:
                    return Response({"detail": "Insufficient Sick leave balance."}, status=status.HTTP_400_BAD_REQUEST)
                balance.sick_used += days
            elif leave_request.leave_type == LeaveType.EMERGENCY:
                if balance.emergency_used + days > balance.emergency_total:
                    return Response({"detail": "Insufficient Emergency leave balance."}, status=status.HTTP_400_BAD_REQUEST)
                balance.emergency_used += days

            balance.save()

        leave_request.status = LeaveStatus.APPROVED
        leave_request.hr_approved_by = request.user
        leave_request.hr_approval_date = timezone.now()
        
        # If manager approval was bypassed (e.g. approved directly by HR)
        if not leave_request.manager_approved_by:
            leave_request.manager_approved_by = request.user
            leave_request.manager_approval_date = timezone.now()

        leave_request.save()

        return Response(LeaveRequestSerializer(leave_request).data)

    @action(detail=True, methods=['post'], url_path='reject', permission_classes=[IsAuthenticated, IsManager])
    def reject(self, request, pk=None):
        leave_request = self.get_object()
        
        # Verify permissions: must be the manager or HR
        if request.user.role not in [Role.SUPER_ADMIN, Role.COMPANY_ADMIN, Role.HR_MANAGER]:
            if leave_request.employee.manager != request.user:
                return Response(
                    {"detail": "You are not authorized to reject this request."},
                    status=status.HTTP_403_FORBIDDEN
                )

        if leave_request.status not in [LeaveStatus.PENDING_MANAGER, LeaveStatus.PENDING_HR]:
            return Response(
                {"detail": "Leave request cannot be rejected from its current status."},
                status=status.HTTP_400_BAD_REQUEST
            )

        rejection_reason = request.data.get('rejection_reason', 'Rejected by manager/HR')
        leave_request.status = LeaveStatus.REJECTED
        leave_request.rejection_reason = rejection_reason
        leave_request.save()

        return Response(LeaveRequestSerializer(leave_request).data)

class LeaveBalanceViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = LeaveBalanceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == Role.SUPER_ADMIN:
            return LeaveBalance.objects.all()
        if user.role in [Role.COMPANY_ADMIN, Role.HR_MANAGER]:
            return LeaveBalance.objects.filter(employee__branch__company=user.company)
        if user.role == Role.MANAGER:
            return LeaveBalance.objects.filter(
                models.Q(employee__manager=user) | models.Q(employee__user=user)
            )
        return LeaveBalance.objects.filter(employee__user=user)
