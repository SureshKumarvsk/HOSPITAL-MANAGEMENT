from django.db import models
import datetime
from django.contrib.auth.models import User


class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True,blank=True,default=0)
    password =models.TextField(default="0")
    email =models.EmailField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')],
        null=True, 
        blank=True
    )
    contact = models.IntegerField(null=True,blank=True,default=0)
    address = models.TextField( null=True,blank=True)
    date = models.CharField(default=datetime.date.today,max_length=200)
    disease_diagnosed = models.CharField(max_length=255,null=True,blank=True)
    case_details = models.TextField(null=True,blank=True) 
    medications = models.TextField(null=True,blank=True)
    Appointment_confirmation = models.CharField(max_length=2,default="0",null=True,blank=True)
    host = models.ForeignKey(User,on_delete=models.CASCADE)



class refcases(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True,blank=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')],
    null=True,blank=True)
    contact = models.IntegerField(null=True,blank=True)
    address = models.TextField(null=True,blank=True)
    date = models.CharField(default=datetime.date.today,max_length=200)
    disease_diagnosed = models.CharField(max_length=255,null=True,blank=True)
    case_details = models.TextField(null=True,blank=True) 
    medications = models.TextField(null=True,blank=True)
    doctor = models.CharField(max_length=100)



class Profile(models.Model):
    image = models.ImageField(default='default.png', upload_to='uploads', null=True, blank=True)
    docter_id = models.CharField(max_length=100,null=True, blank=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(
        max_length=10, 
        choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], 
        null=True, 
        blank=True
    )
    DateOfBirth = models.DateField(default=datetime.date.today, null=True, blank=True)
    contact = models.IntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    address = models.TextField(max_length=200, null=True, blank=True)
    Designation = models.TextField(max_length=200, null=True, blank=True)
    experience = models.IntegerField(default=0, null=True, blank=True)
    NoOfCasesattended = models.IntegerField(null=True, blank=True)



class Appointment(models.Model):
    patient_name = models.CharField(max_length=100)
    disease_diagnosed = models.CharField(max_length=255)
    date = models.CharField(max_length=200) 
    time = models.CharField(max_length=100)
    message_to_doctor = models.TextField()  
    doctor = models.CharField(max_length=10)

class Accept_Model(models.Model):
    patient_name = models.CharField(max_length=100)
    disease_diagnosed = models.CharField(max_length=255)
    date = models.CharField(max_length=200) 
    time = models.CharField(max_length=100)
    message_to_doctor = models.TextField()  
    doctor = models.CharField(max_length=10)

class Decline_Model(models.Model):
    patient_name = models.CharField(max_length=100)
    disease_diagnosed = models.CharField(max_length=255)
    date = models.CharField(max_length=200) 
    time = models.CharField(max_length=100)
    message_to_doctor = models.TextField()  
    doctor = models.CharField(max_length=10)