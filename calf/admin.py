from django.contrib import admin
from .models import Calf
# Register your models here.
class calfModelAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "updated","timestamp"]
	list_filter = ["updated", "timestamp"]
	search_fields = ["calf_Id"]
	class meta:
		model = Calf

admin.site.register(Calf,calfModelAdmin)
admin.site.site_header = 'Paavni Dairy Farms'