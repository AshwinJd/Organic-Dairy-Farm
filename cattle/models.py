from django.db import models
from datetime import date

YES = 'Yes'
NO = 'No'
  
choices = (
    (YES, 'Yes'),
    (NO, 'No'),
)

class Cattle(models.Model):
   
    MALE = "Male"
    FEMALE = "Female"
    MISCARRIAGE = "Fail"
    SAFE = "safe"
    NOT_SAFE = "Not Safe"
    cattle_Id = models.CharField(max_length=15, primary_key=True)
    name = models.CharField(max_length=30, null=False, default='NULL')
    Breed = models.CharField(max_length=30, null=True)
    date_of_birth = models.DateField(null=True, default=date.today)
    age = models.IntegerField(default=0)
    weight = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    gender = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    sex = models.CharField(max_length=8, choices=gender, default = 'U')

    
    
    pno_buyer = models.CharField(max_length=200, null=False, default='NULL')
    pno_seller = models.CharField(max_length=200, null=False, default='NULL')
    dehorning = models.CharField(max_length=4,choices=choices, default=NO)
    Insurance = models.CharField(max_length=4,choices=choices, default=NO)
    date_of_expiry_insurance = models.DateField(null=True)

    # VACCINATION RECORD

    Vaccine_for_Foot_and_Mouth_disease_FMD = models.CharField(max_length = 200, null= False, default='NULL')
    Date_FMD = models.DateField(default=date.today)
    Vaccine_FMD_confirmation = models.CharField(max_length=4,choices=choices, default=NO)

    Vaccine_for_Hemorrhagic_Septicemia_HS = models.CharField(max_length = 200, null= False, default='NULL')
    Date_HS = models.DateField(default=date.today)
    Vaccine_HS_confirmation = models.CharField(max_length=4,choices=choices, default=NO)

    Vaccine_for_Black_Quarter_BQ = models.CharField(max_length = 200, null= False, default='NULL')
    Date_BQ = models.DateField(default=date.today)
    Vaccine_BQ_confirmation = models.CharField(max_length=4,choices=choices, default=NO)

    Vaccine_for_Brucella = models.CharField(max_length = 200, null= False, default='NULL')
    Date_Brucella = models.DateField(default=date.today)
    Vaccine_for_Brucella_confirmation = models.CharField(max_length=4,choices=choices, default=NO)

    Vaccine_for_Theileriosis = models.CharField(max_length = 200, null= False, default='NULL')
    Date_T = models.DateField(default=date.today)
    Vaccine_for_Theileriosis_confirmation = models.CharField(max_length=4,choices=choices, default=NO)

    Deworming_1st_quarter_date = models.DateField(default=date.today)
    Deworming_medicine_name_1 = models.CharField(max_length=200, blank= False, default='NULL')
    Deworming_1st_quarter_confirmation = models.CharField(max_length=4,choices=choices,default = NO)
    Deworming_2nd_quarter_date = models.DateField(default=date.today)
    Deworming_medicine_name_2 = models.CharField(max_length=200, blank= False, default='NULL')
    Deworming_2nd_quarter_confirmation = models.CharField(max_length=4,choices=choices,default = NO)
    Deworming_3rd_quarter_date = models.DateField(default=date.today)
    Deworming_medicine_name_3 = models.CharField(max_length=200, blank= False, default='NULL')
    Deworming_3rd_quarter_confirmation = models.CharField(max_length=4,choices=choices,default = NO)
    Deworming_4th_quarter_date = models.DateField(default=date.today)
    Deworming_medicine_name_4 = models.CharField(max_length=200, blank= False, default='NULL')
    Deworming_4th_quarter_confirmation = models.CharField(max_length=4,choices=choices,default = NO)

    # AI RECORD
    Semen_details = models.CharField(max_length=100, blank= False, default='NULL')
    Confirmation_after_oneMonth = models.CharField(max_length=4,choices=choices,default = NO)
    Confirmation_after_threeMonth = models.CharField(max_length=4,choices=choices,default = NO)
    Expected_date_of_Delivery = models.DateField(default=date.today)
    Status = (
        (SAFE, "Safe"),
        (NOT_SAFE, "Not Safe"),
       
    )

    Delivery_status = models.CharField(max_length=8, choices=Status, default=SAFE)

    Delivery = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (MISCARRIAGE, 'Miscarriage'),
    )

    Delivery_calf = models.CharField(max_length=8, choices=Delivery, default=MALE)


    updated = models.DateTimeField(auto_now = True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now = False, auto_now_add = True)

    def __unicode__(self):
        return self.cattle_Id




class HeatRecord(models.Model):
    cattle = models.ForeignKey(Cattle, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)


    def __unicode__(self):
        return self.cattle.cattle_Id

class Entry(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    # name = models.CharField(max-length=30, null=False, default="Null")
    title = models.SlugField(max_length=20, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Chat Entry"
        verbose_name_plural = "Chat Entries"
        ordering = ["-created"]