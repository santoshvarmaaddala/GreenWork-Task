from django.contrib import admin
from .models import Attendance, Performance

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('employee', 'date', 'status')
    list_filter = ('status', 'date', 'employee')

@admin.register(Performance)
class PerformanceAdmin(admin.ModelAdmin):
    list_display = ('employee', 'rating', 'review_date')
    list_filter = ('rating', 'employee')