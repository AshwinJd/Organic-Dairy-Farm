from django import forms
from .models import Invoice

class invoiceform(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['Customer_name', 'Quantity','Rate','Dues','Amount_given','Payment_Date','Payment_details']
