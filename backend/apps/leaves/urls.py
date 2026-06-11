from django.urls import path, include
from rest_framework.routers import DefaultRouter
from leaves.views import LeaveRequestViewSet, LeaveBalanceViewSet

router = DefaultRouter()
router.register('leaves', LeaveRequestViewSet, basename='leave')
router.register('leave-balances', LeaveBalanceViewSet, basename='leave-balance')

urlpatterns = [
    path('', include(router.urls)),
]
