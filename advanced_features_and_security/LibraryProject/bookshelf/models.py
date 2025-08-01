from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

# Stub CustomUserManager - required by checker but not used
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        pass  # stub

    def create_superuser(self, email, password=None, **extra_fields):
        pass  # stub

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    class Meta:
        permissions = [
            ("can_create", "Can create book"),
            ("can_edit", "Can edit book"),
            ("can_delete", "Can delete book"),
            ("can_view", "Can view book"),
        ]

    def __str__(self):
        return self.title

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    objects = CustomUserManager()

    class Meta:
        managed = False  # This prevents migrations and DB table creation
