from django.conf.urls import url
from django.contrib import admin
from customer import views as cust_views
from .models import Customer

     
urlpatterns = [   
    url(r'^$', cust_views.custpage, name='custpage'),
 	url(r'^(?P<Cust_Id>[0-9]+)/$', cust_views.cust_section, name='cust_section'),
]