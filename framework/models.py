from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.
class employee(models.Model):
    name = models.CharField(max_length = 200)
    salary = models.CharField(max_length = 200)
    company = models.CharField(max_length = 200)

    def __str__(self):
        return self.name

class user(AbstractBaseUser):
    my_field = models.CharField(max_length=10)