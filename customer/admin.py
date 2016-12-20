from django.contrib import admin
from .models import Customer
# Register your models here.

class custModelAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "updated","timestamp"]
	list_filter = ["updated", "timestamp"]
	search_fields = ["Cust_Id"]
	class meta:
		model = Customer

admin.site.register(Customer,custModelAdmin)
admin.site.site_header = 'Paavni Dairy Farms'