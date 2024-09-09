from django.db import models


class Employee(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    photo=models.ImageField(upload_to='images')
    designation=models.CharField(max_length=100)
    email=models.EmailField(max_length=100,unique=True)
    phone=models.CharField(max_length=12,blank=True)#optional
    Created_at=models.DateTimeField(auto_now_add=True)
    Updated_at=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.fname


# Create your models here.
