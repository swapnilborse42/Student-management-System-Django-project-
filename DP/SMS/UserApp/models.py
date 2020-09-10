from django.db import models

# Create your models here.
class Depertment(models.Model):
    dname = models.CharField(max_length=100)

    def __str__(self):
        return self.dname

class Dclass(models.Model):
    dcname = models.CharField(max_length=100)
    dname = models.ForeignKey(Depertment,on_delete="models.CASCADE")
    def __str__(self):
        return self.dcname

class Studs(models.Model):
    sname=models.CharField(max_length=100)
    dname =models.ForeignKey(Depertment,on_delete="models.CASCADE")

    def __str__(self):
        return self.sname

class Subject(models.Model):
    subname=models.CharField(max_length=100)
    dname =models.ForeignKey(Depertment,on_delete="models.CASCADE")
    students = models.ManyToManyField(Studs)
    def __str__(self):
        return self.subname

class Teacher(models.Model):
    tname=models.CharField(max_length=100)
    dname =models.ForeignKey(Depertment,on_delete="models.CASCADE")
    #tecaches=models.OneToManyFields(Subject,on_delete="models.CASCADE")
    student2 = models.ManyToManyField(Studs)

    def __str__(self):
        return self.tname




dd = Dclass.objects.all()
print(dd)

dd1 = Depertment.objects.all()
print(dd1)
