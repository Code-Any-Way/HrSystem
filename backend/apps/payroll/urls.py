from django.urls import path, include
from rest_framework.routers import DefaultRouter
from payroll.views import PayrollRunViewSet, PayrollDetailViewSet

router = DefaultRouter()
router.register('payroll-runs', PayrollRunViewSet, basename='payroll-run')
router.register('payroll-details', PayrollDetailViewSet, basename='payroll-detail')

urlpatterns = [
    path('', include(router.urls)),
]
