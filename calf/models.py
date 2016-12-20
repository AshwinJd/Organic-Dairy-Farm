from __future__ import unicode_literals

from django.db import models
from datetime import date

# Create your models here.
class Calf(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    YES ='Yes'
    NO = 'No'
    choices = (
    (YES, 'Yes'),
    (NO, 'No'),
    )

    calf_Id = models.CharField(max_length=15, primary_key=True)
    name = models.CharField(max_length=30, null=False, default='NULL')
    Breed = models.CharField(max_length=30)
    date_of_birth = models.DateField(null=True, default=date.today)
    age = models.IntegerField(default=0)
    weight = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    gender = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    sex = models.CharField(max_length=8, choices=gender, default = 'U')

        
    pno_buyer = models.CharField(max_length=200, null=False, default='NULL')
    pno_seller = models.CharField(max_length=200, null=False, default='NULL')
    
    Insurance = models.CharField(max_length=4,choices=choices, default=NO)
    date_of_expiry_insurance = models.DateField(null=True)

    # VACCINATION RECORD
    dehorning = models.CharField(max_length=4,choices=choices, default=NO, )
    One_time_Vaccination = models.CharField(max_length=4,choices=choices,default = NO)
    Remarks = models.TextField(null=False, default='NULL')

    updated = models.DateTimeField(auto_now = True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now = False, auto_now_add = True)

    def __unicode__(self):
        return self.calf_Id