from rest_framework import viewsets, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from django.db import models
from django_filters.rest_framework import DjangoFilterBackend
from accounts.models import Role
from employees.models import Employee
from attendance.models import Attendance, AttendanceStatus
from attendance.serializers import (
    AttendanceSerializer, 
    CheckInSerializer, 
    CheckOutSerializer
)

class AttendanceViewSet(viewsets.ModelViewSet):
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['date', 'status', 'employee']
    ordering_fields = ['date', 'check_in']

    def get_queryset(self):
        user = self.request.user
        if user.role == Role.SUPER_ADMIN:
            return Attendance.objects.all()
        # HR and Company Admins see their company's attendance records
        if user.role in [Role.COMPANY_ADMIN, Role.HR_MANAGER]:
            return Attendance.objects.filter(employee__branch__company=user.company)
        # Managers view their team members' + their own records
        if user.role == Role.MANAGER:
            return Attendance.objects.filter(
                models.Q(employee__manager=user) | models.Q(employee__user=user)
            )
        # Employees view their own records
        return Attendance.objects.filter(employee__user=user)

    @action(detail=False, methods=['post'], url_path='check-in')
    def check_in(self, request):
        try:
            employee = Employee.objects.get(user=request.user)
        except Employee.DoesNotExist:
            return Response(
                {"detail": "No employee profile found for current user."},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        today = timezone.localdate()
        if Attendance.objects.filter(employee=employee, date=today).exists():
            return Response(
                {"detail": "You have already checked in today."},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        serializer = CheckInSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Late check-in logic (lateness starts after 09:00 AM)
        now = timezone.localtime()
        status_val = AttendanceStatus.PRESENT
        if now.hour > 9 or (now.hour == 9 and now.minute > 0):
            status_val = AttendanceStatus.LATE
            
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        ip = x_forwarded_for.split(',')[0].strip() if x_forwarded_for else request.META.get('REMOTE_ADDR')

        attendance = Attendance.objects.create(
            employee=employee,
            date=today,
            check_in=now,
            status=status_val,
            gps_lat_in=serializer.validated_data.get('gps_lat'),
            gps_lng_in=serializer.validated_data.get('gps_lng'),
            qr_token=serializer.validated_data.get('qr_token'),
            ip_address=ip
        )
        return Response(AttendanceSerializer(attendance).data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'], url_path='check-out')
    def check_out(self, request):
        try:
            employee = Employee.objects.get(user=request.user)
        except Employee.DoesNotExist:
            return Response(
                {"detail": "No employee profile found for current user."},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        today = timezone.localdate()
        attendance = Attendance.objects.filter(employee=employee, date=today).first()
        
        if not attendance:
            return Response(
                {"detail": "No check-in record found for today."},
                status=status.HTTP_400_BAD_REQUEST
            )
        if attendance.check_out:
            return Response(
                {"detail": "You have already checked out today."},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        serializer = CheckOutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        attendance.check_out = timezone.localtime()
        attendance.gps_lat_out = serializer.validated_data.get('gps_lat')
        attendance.gps_lng_out = serializer.validated_data.get('gps_lng')
        attendance.save()
        
        return Response(AttendanceSerializer(attendance).data, status=status.HTTP_200_OK)
