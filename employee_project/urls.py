from django.urls import path, include
from django.contrib import admin
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from employees.views import (
    login_view,
    logout_view,
    SignupView,
    home_view,
    AnalyticsView,
    DepartmentStatsView,
    DepartmentStats,
    MonthlyAttendanceStats
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Template Auth Views
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('home/', home_view, name='home'),
    path('analytics/', AnalyticsView.as_view(), name='analytics'),
    path('analytics/dept-stats/', DepartmentStatsView.as_view(), name='department-stats'),

    # API Views (JWT required)
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/department-stats/', DepartmentStats.as_view(), name='department-stats-api'),
    path('api/attendance-stats/', MonthlyAttendanceStats.as_view(), name='attendance-stats-api'),
    
    # Swagger UI
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]