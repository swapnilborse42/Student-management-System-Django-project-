from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Stud(models.Model):

    prn = models.IntegerField()
    name = models.CharField(max_length=100)
    cls = models.CharField(max_length=100)
    dept = models.CharField(max_length=100)
