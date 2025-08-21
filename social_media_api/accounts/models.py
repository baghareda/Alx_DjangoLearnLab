from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    # followers = who follows ME
    followers = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='following',  # so I can access who I follow via user.following.all()
        blank=True
    )

    def __str__(self):
        return self.username
