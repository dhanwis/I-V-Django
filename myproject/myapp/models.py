from django.db import models


class Student(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField(verbose_name='Age')
    email=models.EmailField(verbose_name='Email')
    dob=models.DateField(verbose_name='DOB')  
