from rest_framework import viewsets, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Avg, Q
from django_filters.rest_framework import DjangoFilterBackend

from accounts.models import Role
from accounts.permissions import IsHRManager, IsManager
from employees.models import Employee
from evaluations.models import PerformanceEvaluation
from evaluations.serializers import PerformanceEvaluationSerializer

class PerformanceEvaluationViewSet(viewsets.ModelViewSet):
    serializer_class = PerformanceEvaluationSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['employee', 'evaluation_period']
    ordering_fields = ['score', 'created_at']

    def get_permissions(self):
        # Only managers and HR can write evaluations
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAuthenticated(), IsManager()]
        return [IsAuthenticated()]

    def get_queryset(self):
        user = self.request.user
        if user.role == Role.SUPER_ADMIN:
            return PerformanceEvaluation.objects.all()
        # HR and Company Admin view all evaluations in their company
        if user.role in [Role.COMPANY_ADMIN, Role.HR_MANAGER]:
            return PerformanceEvaluation.objects.filter(employee__branch__company=user.company)
        # Managers view evaluations they authored or those for their team members
        if user.role == Role.MANAGER:
            return PerformanceEvaluation.objects.filter(
                Q(evaluator=user) | Q(employee__manager=user)
            )
        # Employees view only their own evaluations
        return PerformanceEvaluation.objects.filter(employee__user=user)

    def perform_create(self, serializer):
        serializer.save(evaluator=self.request.user)

    @action(detail=False, methods=['get'], url_path='rankings', permission_classes=[IsAuthenticated, IsManager])
    def rankings(self, request):
        """
        Aggregate scoring report ranking employees in active company
        by their average evaluation score.
        """
        user = request.user
        queryset = Employee.objects.all()
        
        if user.role != Role.SUPER_ADMIN and user.company:
            queryset = queryset.filter(branch__company=user.company)
            
        queryset = queryset.annotate(
            avg_score=Avg('evaluations__score')
        ).filter(avg_score__isnull=False).order_by('-avg_score')
        
        rankings_data = []
        for rank, emp in enumerate(queryset, 1):
            rankings_data.append({
                "rank": rank,
                "employee_id": emp.id,
                "employee_code": emp.employee_code,
                "first_name": emp.first_name,
                "last_name": emp.last_name,
                "job_title": emp.job_title,
                "department_name": emp.department.name,
                "average_score": round(emp.avg_score, 2)
            })
            
        return Response(rankings_data)
