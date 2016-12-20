from django.contrib import admin
from .models import Invoice
# Register your models here.
class invoiceModelAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "Date"]
	list_filter = ["Customer_name", "Date",]
	search_fields = ["Customer_name"]

	class meta:
		model = Invoice

admin.site.register(Invoice,invoiceModelAdmin)
admin.site.site_header = 'Paavni Dairy Farms'