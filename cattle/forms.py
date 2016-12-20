from django import forms
from .models import Entry

class notifyform(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['title','body']
