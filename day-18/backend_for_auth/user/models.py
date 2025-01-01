from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    bio = models.CharField(max_length=255,blank=True)
    cover_photo = models.ImageField(upload_to='images/',blank=True,null=True)
    id_number = models.IntegerField(null=True, blank=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_groups',  # Unique related_name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',  # Unique related_name
        blank=True
    )
    def __str__(self):
        return self.username