from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Customer(models.Model):
    Cust_Id = models.CharField(max_length=15, primary_key=True)
    Cust_Name = models.CharField(max_length=30, null=False, default='NULL')
    Cust_address = models.CharField(max_length=80, null=False, default='NULL')
    contact = models.CharField(max_length=15, null=False, default='NULL')
    Email_Id = models.CharField(max_length=25, null=False, default='NULL')
    Payment_Dues = models.IntegerField(default=0)
    Usual_purchase_details = models.TextField(null=False, default='NULL')

    updated = models.DateTimeField(auto_now = True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now = False, auto_now_add = True)

    def __unicode__(self):
        return self.Cust_Id