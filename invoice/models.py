from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Invoice(models.Model):
    Customer_name = models.CharField(max_length = 50, null= False)
    Date = models.DateField(auto_now_add=True)
    Quantity = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    Rate = models.DecimalField(max_digits=7, decimal_places=2, default=12.50)
    Dues = models.IntegerField(default=0)
    Amount_given = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    Total_amt = models.DecimalField(max_digits=7, decimal_places=2, default=0)
  
    New_Dues = models.DecimalField(max_digits=7, decimal_places=2 ,default=0)

    def save(self):
        self.Total_amt = (self.Rate * self.Quantity) + self.Dues
        self.New_Dues = self.Total_amt - self.Amount_given
        super(Invoice, self).save()
    
    Payment_Date = models.DateField(auto_now=False)
    Payment_methods = (
        ('CASH', 'Cash'),
        ('OTHERS', 'Others'),
    )
    Payment_details= models.CharField(max_length = 6,choices=Payment_methods, default='CASH')
    def __unicode__(self):
        return self.Customer_name

