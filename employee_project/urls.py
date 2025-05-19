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
    DepartmentStats,
    MonthlyAttendanceStats,
    AttendanceReportView
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Template Auth Views
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('home/', home_view, name='home'),
    path('analytics/', AnalyticsView.as_view(), name='analytics'),

    # API Views (JWT required)
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('analytics/dept-data/', DepartmentStats.as_view(), name='dept_data'),
    path('analytics/attendance-data/', MonthlyAttendanceStats.as_view(), name='attendance_data'),
    path('attendance/report/', AttendanceReportView.as_view(), name='attendance_report'),
   
    
    # Swagger UI
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]