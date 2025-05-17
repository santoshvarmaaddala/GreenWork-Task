from django.urls import path
from .views import MyTokenObtainPairView
from .views import AdminOnlyView, HRProtectedView, login_view, logout_view, SignupView, HomeView, test_session

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', SignupView, name='signup'),
    path('home/', HomeView.as_view(), name='home'),
    path('test-session/', test_session),

    # JWT Token URLs
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
]