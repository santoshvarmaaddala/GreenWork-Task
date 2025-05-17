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