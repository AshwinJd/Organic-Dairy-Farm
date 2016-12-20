from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Cattle, Entry
from .forms import notifyform


def home(request):
	all_blog = Entry.objects.all()[0:5]

	return render(request, "index.html" , {'all_blog': all_blog})
	

def log_in(request):
	return render(request, "login.html",{})

def cattlepage(request):
	all_cattle = Cattle.objects.all()

	context = {
		'all_cattle' : all_cattle,
		
	}
	return render(request,'cattlepage.html', context)


def cattle_section(request,cattle_Id):
	
	try:
		cattle_data = Cattle.objects.get(pk = cattle_Id)
	except Cattle.DoesNotExist:
		raise Http404("The Cattle info doesn't exist")
	context = {
		'cattle_data' : cattle_data,
			}
	return render(request, "cattle_data.html",context)

def notifypage(request):
	form = notifyform(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect('/')
	context = {
		'form': form
	}
	return render(request, 'notifyentry.html',context)