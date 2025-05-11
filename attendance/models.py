from django.db import models
from employees.models import Employee

class Attendance(models.Model):
    STATUS_CHOICES = (
        ('Present', 'Present'),
        ('Absent', 'Absent'),
        ('Late', 'Late'),
    )

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='attendance_records')
    date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    class Meta:
        unique_together = ('employee', 'date')  # One record per employee per day

    def __str__(self):
        return f"{self.employee.name} - {self.date}: {self.status}"


class Performance(models.Model):
    RATING_CHOICES = (
        (1, '1 - Poor'),
        (2, '2 - Fair'),
        (3, '3 - Good'),
        (4, '4 - Very Good'),
        (5, '5 - Excellent'),
    )

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='performance_reviews')
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES)
    review_date = models.DateField()

    def __str__(self):
        return f"{self.employee.name} - Rating: {self.rating}"