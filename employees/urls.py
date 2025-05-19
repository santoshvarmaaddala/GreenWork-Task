from django.urls import path
from .views import (
    login_view,
    logout_view,
    SignupView,
    home_view,
    test_session,
)
from employees.views import AttendanceFormView

app_name = 'employees'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('home/', home_view, name='home'),
     path('attendance/', AttendanceFormView.as_view(), name='mark_attendance'),
    path('test-session/', test_session, name='test_session'),
]