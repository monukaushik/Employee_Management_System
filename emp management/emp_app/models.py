from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from .manager import *

class Userdetail(AbstractBaseUser,PermissionsMixin):
        email=models.EmailField(unique=True)
        username=models.CharField(max_length=100)
        department=models.CharField(max_length=100)
        employeename=models.CharField(max_length=100)
        employeepic=models.ImageField(upload_to='images/')
        fathername=models.CharField(max_length=100)
        mothername=models.CharField(max_length=100)
        employeeid=models.CharField(max_length=100)
        employeedegination=models.CharField(max_length=200)
        joiningdate=models.DateField(null=True)
        employeeleave=models.IntegerField(null=True)
        employeesalary=models.IntegerField(null=True)
        employeecontect=models.IntegerField(null=True)
        employeeaddress=models.CharField(max_length=200)
        Key=models.CharField(max_length=200,null=True)

        is_active = models.BooleanField(default=True)
        is_staff = models.BooleanField(default=False)

        objects=CustomuserdetailManager()
        USERNAME_FIELD='email'
        REQUIRED_FIELDS=['username','department']

        def __str__(self):
            return self.email 

class leaveinformation(models.Model):
    id=models.IntegerField(primary_key=True)
    managername=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    applyleave=models.IntegerField(null=True)
    leavepurpose=models.CharField(max_length=200)
    leavedatefrom=models.DateField(null=True)
    leavedateto=models.DateField(null=True)
    leavestatus=models.CharField(max_length=100,default='pending')


