from rest_framework import serializers
from evaluations.models import PerformanceEvaluation
from employees.serializers import EmployeeMiniSerializer

class PerformanceEvaluationSerializer(serializers.ModelSerializer):
    employee_details = EmployeeMiniSerializer(source='employee', read_only=True)
    evaluator_name = serializers.SerializerMethodField()

    class Meta:
        model = PerformanceEvaluation
        fields = [
            'id', 'employee', 'employee_details', 'evaluator', 'evaluator_name', 
            'score', 'evaluation_period', 'notes', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'evaluator']

    def get_evaluator_name(self, obj):
        return f"{obj.evaluator.first_name} {obj.evaluator.last_name}".strip() or obj.evaluator.email
