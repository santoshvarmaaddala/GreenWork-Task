from rest_framework import viewsets
from .models import Attendance, Performance
from .serializers import AttendanceSerializer, PerformanceSerializer
from .permissions import IsHR, IsAdminOrHR
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [IsHR]  # Only HR can edit attendance

class PerformanceViewSet(viewsets.ModelViewSet):
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer
    permission_classes = [IsAdminOrHR]

class HRProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.role != 'hr':
            return Response(
                {"detail": "You do not have permission to access this resource."},
                status=status.HTTP_403_FORBIDDEN
            )
        return Response({"message": "Welcome HR!"})