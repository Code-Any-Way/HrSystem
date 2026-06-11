from django.urls import path, include
from rest_framework.routers import DefaultRouter
from assets.views import AssetViewSet, AssetAssignmentViewSet

router = DefaultRouter()
router.register('assets', AssetViewSet, basename='asset')
router.register('asset-assignments', AssetAssignmentViewSet, basename='asset-assignment')

urlpatterns = [
    path('', include(router.urls)),
]
