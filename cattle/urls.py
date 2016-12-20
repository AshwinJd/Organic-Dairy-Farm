from django.conf.urls import url
from django.contrib import admin
from cattle import views as cattle_views
from .models import Cattle

urlpatterns = [
   
 	url(r'^$',cattle_views.home, name="home" ),
 	url(r'^cattlepage/', cattle_views.cattlepage, name='cattlepage'),
 	url(r'^notifypage/', cattle_views.notifypage, name='notifypage'),
 	url(r'^(?P<cattle_Id>[0-9]+)/$', cattle_views.cattle_section, name='cattle_section'),

 	]
