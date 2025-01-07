import uuid

from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

from authentication.managers import Manager


class User(AbstractBaseUser):
    # User personal data
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4)
    username = models.CharField(max_length=50, blank=True)

    # Auth
    email = models.EmailField(blank=False, null=False, unique=True)

    # User status
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    # Model data
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    # REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = Manager()

    def __str__(self):
        return self.email

    class Meta:
        db_table = "users"
