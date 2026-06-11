from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # API Documentation
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/docs/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    
    # API endpoints
    path('api/auth/', include('accounts.urls')),
    path('api/', include('companies.urls')),
    path('api/', include('departments.urls')),
    path('api/', include('teams.urls')),
    path('api/', include('employees.urls')),
    path('api/', include('attendance.urls')),
    path('api/', include('leaves.urls')),
    path('api/', include('payroll.urls')),
    path('api/', include('assets.urls')),
    path('api/', include('expenses.urls')),
    path('api/', include('evaluations.urls')),
    path('api/', include('notifications.urls')),
    path('api/', include('audit_logs.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
