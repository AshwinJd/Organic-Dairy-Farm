from django.shortcuts import render


from .models import Customer
# Create your views here.
def custpage(request):
	all_cust = Customer.objects.all()

	context = {
		'all_cust' : all_cust,
		
	}
	return render(request,'custpage.html', context)
def cust_section(request,Cust_Id):
	
	try:
		cust_data = Customer.objects.get(pk = Cust_Id)
	except Customer.DoesNotExist:
		raise Http404("The Customer info doesn't exist")
	context = {
		'cust_data' : cust_data,
			}
	return render(request, "cust_data.html",context)

