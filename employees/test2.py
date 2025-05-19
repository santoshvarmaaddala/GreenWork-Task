from django.test import TestCase
from django.urls import reverse
from .models import Employee, Department
from attendance.models import Attendance

class AuthTests(TestCase):
    def test_login_page_status_code(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)

    def test_home_redirect_if_not_logged_in(self):
        response = self.client.get('/home/', follow=True)
        self.assertRedirects(response, '/login/?next=/home/')

    def test_home_access_when_logged_in(self):
        dept = Department.objects.create(name="Engineering")
        user = Employee.objects.create_user(
            email='test@example.com',
            password='password123',
            department=dept,
            role='employee'
        )
        login_success = self.client.login(email='test@example.com', password='password123')
        self.assertTrue(login_success)

        response = self.client.get('/home/')
        self.assertEqual(response.status_code, 200)