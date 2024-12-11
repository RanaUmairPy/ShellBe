
from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager  


class CUser(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True)
    user_profile = models.ImageField(upload_to='profile_pic', blank=True, null=True)
    email = models.EmailField(unique=True)

   
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number', 'username']

    objects = CustomUserManager()  

    def __str__(self):
        return self.email
