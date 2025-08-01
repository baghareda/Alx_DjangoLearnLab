from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)
    
     objects = CustomUserManager()
     
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        pass

    def create_superuser(self, email, password=None, **extra_fields):
        pass
