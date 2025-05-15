from django.urls import path
from .views import MyTokenObtainPairView
from .views import AdminOnlyView, HRProtectedView

urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('admin-only/', AdminOnlyView.as_view(), name='admin_only'),
    path('hr-only/', HRProtectedView.as_view(), name='hr_only'),
]
