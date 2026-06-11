from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from accounts.models import Role
from accounts.permissions import IsHRManager
from teams.models import Team
from teams.serializers import TeamSerializer

class TeamViewSet(viewsets.ModelViewSet):
    serializer_class = TeamSerializer
    permission_classes = [IsAuthenticated, IsHRManager]

    def get_queryset(self):
        user = self.request.user
        if user.role == Role.SUPER_ADMIN:
            return Team.objects.all()
        if user.company:
            return Team.objects.filter(department__company=user.company)
        return Team.objects.none()
