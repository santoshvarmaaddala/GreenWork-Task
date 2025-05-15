from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import EmployeeManager
from datetime import date
class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name


class Employee(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('hr', 'HR'),
        ('manager', 'Manager'),
        ('employee', 'Employee'),
    )

    # Override email to make it required and unique
    email = models.EmailField(
        verbose_name='Email',
        max_length=255,
        unique=True,
    )

    name = models.CharField(max_length=150)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='employee')
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(null=True, blank=True, default=date.today)
    date_of_joining = models.DateField(null=True, blank=True)
    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        related_name='employees'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # No extra fields needed for createsuperuser

    objects = EmployeeManager()  # 👈 New line added

    def __str__(self):
        return f"{self.name} ({self.department.name if self.department else 'No Department'})"