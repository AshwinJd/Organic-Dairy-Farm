from django.contrib import admin
from .models import Cattle
from .models import HeatRecord, Entry
# Register your models here.

class cattleModelAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "updated","timestamp"]
	list_filter = ["updated", "timestamp","weight"]
	search_fields = ["cattle_Id"]
	class meta:
		model = Cattle



class heatModelAdmin(admin.ModelAdmin):
	list_display = ["__unicode__","date"]
	list_filter = ["cattle"]

	class meta:
		model = HeatRecord

class EntryAdmin(admin.ModelAdmin):
    list_display = ("title", "created")
    prepopulated_fields = {"title": ("body",)}


admin.site.register(Entry, EntryAdmin)
admin.site.register(Cattle, cattleModelAdmin)
admin.site.register(HeatRecord,heatModelAdmin)
admin.site.site_header = 'Paavni Dairy Farms'