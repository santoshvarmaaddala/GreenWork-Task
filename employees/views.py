from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .serializers import LoginSerializer
from rest_framework.permissions import IsAuthenticated
from employees.permissions import IsAdmin, IsHR
from rest_framework import viewsets
from .serializers import EmployeeSerializer, DepartmentSerializer
from .models import Employee, Department
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib.auth.decorators import login_required
from employees.models import Department
from django.db.models import Count
from django.http import JsonResponse

# Optional: Custom token response to include role
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['role'] = user.role
        token['email'] = user.email
        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class AdminOnlyView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]

    def get(self, request):
        return Response({"message": "Welcome Admin!"})

class HRProtectedView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        if request.user.role != 'hr':
            return Response({"detail": "You do not have permission to access this resource."},
                            status=status.HTTP_403_FORBIDDEN)
        return Response({"message": "Welcome HR!"})
    
class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

@never_cache
def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            # print("Redirecting to:", reverse('employees:home'))
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')


@never_cache
@login_required(login_url='/login/')
def home_view(request):
    return render(request, 'home.html', {'user': request.user})


def logout_view(request):
    from django.contrib.auth import logout
    logout(request)
    response = redirect('login')
    response.delete_cookie('sessionid')
    response.delete_cookie('csrftoken')
    return response

class SignupView(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        name = request.POST.get('name')

        if not email or not password1 or not name:
            return render(request, 'signup.html', {'error': 'All fields are required.'})

        if password1 != password2:
            return render(request, 'signup.html', {'error': 'Passwords do not match.'})

        if Employee.objects.filter(email=email).exists():
            return render(request, 'signup.html', {'error': 'Email already exists.'})

        # Create user
        user = Employee.objects.create_user(
            email=email,
            password=password1,
            name=name,
            role='employee'  # Default role for signup
        )
        login(request, user)
        return redirect('home')

def test_session(request):
    print("🔍 Session ID:", request.session.session_key)
    print("👤 User in session:", request.user)
    return Response({"session": request.session.session_key, "user": str(request.user)})

class AnalyticsView(View):
    def get(self, request):
        return render(request, 'analytics.html')


# API endpoint for Chart.js
class DepartmentStatsView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return JsonResponse({'error': 'Authentication required'}, status=401)

        if request.user.role not in ['hr', 'admin']:
            return JsonResponse({'error': 'You do not have permission to access this resource.'}, status=403)

        departments = Department.objects.annotate(employee_count=Count('employees'))
        data = [{'name': d.name, 'employee_count': d.employee_count} for d in departments]
        return JsonResponse(data, safe=False)