from django.urls import path
from attendance import views

urlpatterns = [
    path('hr-only/', views.HRProtectedView.as_view(), name='attendance_hr_only'),
]