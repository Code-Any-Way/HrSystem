from django.urls import path, include
from rest_framework.routers import DefaultRouter
from evaluations.views import PerformanceEvaluationViewSet

router = DefaultRouter()
router.register('evaluations', PerformanceEvaluationViewSet, basename='evaluation')

urlpatterns = [
    path('', include(router.urls)),
]
