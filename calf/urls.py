from django.conf.urls import url
from django.contrib import admin
from calf import views as calf_views
from .models import Calf

     
urlpatterns = [   
    url(r'^$', calf_views.calfpage, name='calfpage'),
 	url(r'^(?P<calf_Id>[0-9]+)/$', calf_views.calf_section, name='calf_section'),
]