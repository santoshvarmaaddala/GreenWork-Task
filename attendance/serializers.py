from rest_framework import serializers
from employees.models import Employee
from .models import Attendance, Performance

class AttendanceSerializer(serializers.ModelSerializer):
    employee = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Attendance
        fields = '__all__'
        extra_kwargs = {
            'employee': {'read_only': True}
        }

    def create(self, validated_data):
        request = self.context.get('request')
        employee_id = request.data.get('employee')
        try:
            employee = Employee.objects.get(id=employee_id)
        except Employee.DoesNotExist:
            raise serializers.ValidationError("Employee does not exist")

        return Attendance.objects.create(employee=employee, **validated_data)


class PerformanceSerializer(serializers.ModelSerializer):
    employee = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Performance
        fields = '__all__'