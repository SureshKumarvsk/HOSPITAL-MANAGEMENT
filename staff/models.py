from django.db import models
import datetime


class Staff_Profile(models.Model):
    image = models.ImageField(default='default.png', upload_to='uploads', null=True, blank=True)
    name = models.CharField(max_length=100)
    password =models.TextField(default="0")
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
   