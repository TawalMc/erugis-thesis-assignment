import uuid

from django.db import models

from authentication.models import User


class Supervisor(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    username = models.CharField(max_length=50, blank=True, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "supervisors"
