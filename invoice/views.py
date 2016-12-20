from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from .forms import invoiceform
from .models import Invoice

# Create your views here.
def invoicepage(request):
    if request.method == "POST":
        form = invoiceform(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # post.Date = timezone.now()
            post.save()
            return redirect('/invoicepage/invoice_detail')
    else:
        form = invoiceform()
    return render(request,"invoicepage.html",{'form':form})

def invoice_detail(request):
  
    invoice_data = Invoice.objects.latest('id')
    return render(request,"invoice_details.html",{'invoice_data':invoice_data})