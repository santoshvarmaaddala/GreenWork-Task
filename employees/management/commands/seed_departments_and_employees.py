from django.core.management.base import BaseCommand
from employees.models import Department, Employee
from attendance.models import Attendance, Performance
from datetime import date, timedelta
import random


class Command(BaseCommand):
    help = "Seeds departments, employees, attendance, and performance data"

    def handle(self, *args, **kwargs):
        # Seed departments
        dept_names = ["Engineering", "Marketing", "Human Resources", "Finance", "Sales"]
        depts = []
        for name in dept_names:
            dept, created = Department.objects.get_or_create(name=name)
            depts.append(dept)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created department: {name}"))
            else:
                self.stdout.write(f"Department {name} already exists.")

        self.stdout.write(self.style.SUCCESS("Departments ensured.\n"))

        # Seed employees
        employees_data = [
            {"name": "Alice Johnson", "email": "alice@example.com"},
            {"name": "Bob Smith", "email": "bob@example.com"},
            {"name": "Charlie Brown", "email": "charlie@example.com"},
            {"name": "Diana Prince", "email": "diana@example.com"},
            {"name": "Ethan Hunt", "email": "ethan@example.com"},
        ]

        employees = []
        for i, emp_data in enumerate(employees_data):
            emp, created = Employee.objects.get_or_create(
                email=emp_data["email"],
                defaults={
                    "name": emp_data["name"],
                    "phone_number": f"+123456789{i+1}",
                    "address": f"{i*100 + 10} Main St",
                    "date_of_joining": date(2020, 1, 1),
                    "department": random.choice(depts),
                },
            )
            employees.append(emp)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created employee: {emp.name}"))

        self.stdout.write(self.style.SUCCESS("Employees seeded.\n"))

        # Seed attendance (last 7 days)
        today = date.today()
        for emp in employees:
            for i in range(7):
                Attendance.objects.get_or_create(
                    employee=emp,
                    date=today - timedelta(days=i),
                    defaults={"status": random.choice(["Present", "Absent", "Late"])},
                )
        self.stdout.write(self.style.SUCCESS("Attendance records seeded.\n"))

        # Seed performance reviews (one per employee)
        for emp in employees:
            Performance.objects.get_or_create(
                employee=emp,
                review_date=date.today(),
                defaults={"rating": random.randint(1, 5)},
            )
        self.stdout.write(self.style.SUCCESS("Performance reviews seeded.\n"))

        self.stdout.write(self.style.SUCCESS("✅ All data seeded successfully."))