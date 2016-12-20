from django.conf.urls import url
from django.contrib import admin
from invoice import views as invoice_views
from .models import Invoice

     
urlpatterns = [   
    url(r'^$', invoice_views.invoicepage, name='invoicepage'),
    url(r'^invoice_detail/$', invoice_views.invoice_detail, name='invoicedetail'),    
]