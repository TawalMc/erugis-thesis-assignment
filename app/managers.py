from django.contrib.auth.base_user import BaseUserManager


class Manager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_admin", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_admin") is not True:
            raise ValueError("Admin must have is_admin=True")
        if extra_fields.get("is_active") is not True:
            raise ValueError("Admin must have is_active=True")

        return self.create_user(email, password, **extra_fields)
