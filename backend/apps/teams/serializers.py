from rest_framework import serializers
from teams.models import Team

class TeamSerializer(serializers.ModelSerializer):
    department_name = serializers.ReadOnlyField(source='department.name')
    leader_name = serializers.SerializerMethodField()

    class Meta:
        model = Team
        fields = ['id', 'department', 'department_name', 'name', 'leader', 'leader_name', 'created_at', 'updated_at']

    def get_leader_name(self, obj):
        if obj.leader:
            return f"{obj.leader.first_name} {obj.leader.last_name}".strip() or obj.leader.email
        return None
