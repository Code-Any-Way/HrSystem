from django.urls import path, include
from rest_framework.routers import DefaultRouter
from companies.views import CompanyViewSet, BranchViewSet

router = DefaultRouter()
router.register('companies', CompanyViewSet, basename='company')
router.register('branches', BranchViewSet, basename='branch')

urlpatterns = [
    path('', include(router.urls)),
]
