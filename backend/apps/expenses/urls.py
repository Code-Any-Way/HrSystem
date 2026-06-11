from django.urls import path, include
from rest_framework.routers import DefaultRouter
from expenses.views import ExpenseRequestViewSet

router = DefaultRouter()
router.register('expenses', ExpenseRequestViewSet, basename='expense')

urlpatterns = [
    path('', include(router.urls)),
]
