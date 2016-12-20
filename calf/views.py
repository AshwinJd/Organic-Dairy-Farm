from django.shortcuts import render
from .models import Calf
# Create your views here.
def calfpage(request):
	all_calf = Calf.objects.all()

	context = {
		'all_calf' : all_calf,
		
	}
	return render(request,'calfpage.html', context)
def calf_section(request,calf_Id):
	
	try:
		calf_data = Calf.objects.get(pk = calf_Id)
	except Calf.DoesNotExist:
		raise Http404("The Cattle info doesn't exist")
	context = {
		'calf_data' : calf_data,
			}
	return render(request, "calf_data.html",context)

