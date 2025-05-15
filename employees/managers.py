from django.contrib.auth.models import UserManager

class EmployeeManager(UserManager):
    def create_superuser(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        return super().create_superuser(username=email, email=email, password=password, **extra_fields)