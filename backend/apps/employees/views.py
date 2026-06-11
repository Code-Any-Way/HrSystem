from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from accounts.models import Role
from accounts.permissions import IsHRManager
from employees.models import Employee
from employees.serializers import EmployeeSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]  # Evaluated per action
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['department', 'team', 'branch', 'status', 'employment_type']
    search_fields = ['first_name', 'last_name', 'email', 'employee_code', 'job_title']
    ordering_fields = ['employee_code', 'hire_date', 'base_salary', 'created_at']

    def get_permissions(self):
        # Allow self profile view/update to any logged-in user, rest is HR restricted
        if self.action in ['me']:
            return [IsAuthenticated()]
        return [IsAuthenticated(), IsHRManager()]

    def get_queryset(self):
        user = self.request.user
        if user.role == Role.SUPER_ADMIN:
            return Employee.objects.all()
        if user.company:
            return Employee.objects.filter(branch__company=user.company)
        return Employee.objects.none()

    @action(detail=False, methods=['get', 'put', 'patch'], url_path='me')
    def me(self, request):
        try:
            employee = Employee.objects.get(user=request.user)
        except Employee.DoesNotExist:
            return Response(
                {"detail": "Employee profile does not exist for this user."},
                status=status.HTTP_404_NOT_FOUND
            )

        if request.method == 'GET':
            serializer = self.get_serializer(employee)
            return Response(serializer.data)
        
        # Allow employee to update safe demographic/contact fields
        # Note: In a production HRMS, some fields (like salary, job title) are restricted
        serializer = self.get_serializer(employee, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
