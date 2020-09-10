from django.contrib.postgres.fields import ArrayField
from django.db import models
from dashboard.models import Student

# Subject_list = {

#     '100' : 'DSA',
#     '101' : 'SPOS',
#     '102' : 'TOC',
#     '103' : 'CN',
# }
# Create your models here.

class Teacher(models.Model):
    objects = models.Manager()
    T_PRN = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name= models.CharField(max_length=50)
    mobile_no = models.CharField(max_length=50)
    email = models.CharField(max_length=50,unique=True)
    gender = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    years = ArrayField(models.IntegerField())
    subjects = models.CharField(max_length=50)
    doj = models.CharField(max_length=50)
    password = models.CharField(max_length=20)

class Subject(models.Model):
    objects = models.Manager()
    sub_id = models.IntegerField(primary_key=True)
    T_PRN = models.ManyToManyField(Teacher)
    sub_name = models.CharField(max_length=50)
    PRN = models.IntegerField(Student)

class Attendance(models.Model):
     objects = models.Manager()
     PRN = models.IntegerField()
     subject_name =models.CharField(max_length=50)
     status = models.CharField(max_length=50)
     date = models.CharField(max_length=50)
     dob=models.CharField(max_length=50)


class Notify(models.Model):
     objects = models.Manager()
     ID=models.IntegerField()
     subject_name =models.CharField(max_length=100)

class Feedback(models.Model):
    objects = models.Manager()
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    feedback=models.CharField(max_length=50)
    





