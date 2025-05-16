from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Employee, Department

class RoleBasedAccessTests(APITestCase):

    def setUp(self):
        self.department = Department.objects.create(name="HR")
        self.hr_user = Employee.objects.create_user(
            email='hr@example.com',
            password='testpass123',
            name='HR User',
            role='hr',
            department=self.department,
            date_of_joining='2025-05-14'
        )
        self.employee_user = Employee.objects.create_user(
            email='emp@example.com',
            password='testpass123',
            name='Employee User',
            role='employee',
            department=self.department,
            date_of_joining='2025-05-14'
        )

    def get_token_for_user(self, user):
        from rest_framework_simplejwt.tokens import RefreshToken
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)

    def test_hr_can_access_hr_only_view(self):
        url = reverse('hr_only')
        token = self.get_token_for_user(self.hr_user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_employee_cannot_access_hr_only_view(self):
        url = reverse('hr_only')
        token = self.get_token_for_user(self.employee_user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)