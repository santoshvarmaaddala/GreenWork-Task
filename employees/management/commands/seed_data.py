import random
from django.core.management.base import BaseCommand
from employees.models import Department, Employee
from attendance.models import Attendance, Performance
from datetime import date, timedelta

class Command(BaseCommand):
    help = 'Seeds the database with sample data for analytics'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding departments...')
        dept_names = ['Engineering', 'Marketing', 'HR', 'Finance', 'Admin']
        departments = []

        for name in dept_names:
            dept, created = Department.objects.get_or_create(name=name)
            departments.append(dept)

        self.stdout.write('Seeding employees...')
        employees = []
        for i in range(50):
            emp = Employee.objects.create_user(
                email=f"employee{i}@example.com",
                password="password123",
                name=f"Employee {i}",
                role=random.choice(['admin', 'hr', 'manager', 'employee']),
                department=random.choice(departments),
                date_of_joining=date.today() - timedelta(days=random.randint(30, 365))
            )
            employees.append(emp)

        self.stdout.write('Seeding attendance records...')
        today = date.today()
        for _ in range(100):
            Attendance.objects.create(
                employee=random.choice(employees),
                date=today - timedelta(days=random.randint(0, 30)),
                status=random.choice(['Present', 'Absent', 'Late'])
            )

        self.stdout.write('Seeding performance reviews...')
        for emp in employees:
            Performance.objects.create(
                employee=emp,
                rating=random.randint(1, 5),
                review_date=date.today()
            )

        self.stdout.write(self.style.SUCCESS('✅ Successfully seeded data'))