from django.db import models

# Create your models here

class Usercreate(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    email= models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    