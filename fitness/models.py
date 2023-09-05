from django.db import models

class Fitnessapp(models.Model):
        firstName=models.CharField(default="",max_length=50)
        middleName=models.CharField(default="",max_length=50)
        lastName=models.CharField(default="",max_length=50)
        gender=models.CharField(default="",max_length=50)
        dateOfBirth=models.CharField(default="",max_length=50)
        department=models.CharField(default="",max_length=50)
        userName=models.CharField(default="",max_length=50)
        email=models.CharField(default="",max_length=50)
        password=models.CharField(default="",max_length=50)
        confirmPassword=models.CharField(default="",max_length=50)


        
