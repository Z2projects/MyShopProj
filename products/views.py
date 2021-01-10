from django.shortcuts import render
from .models import Product
from django.http import HttpResponse

# Create your views here.
def product_entry(request):
    return render(request, 'product_entry.html')

def product_list(request):
    p = Product.objects.all()
    return render(request, 'product_list.html', {'products': p})

def product_save(request):
    pn = request.POST["product_name"]
    r = request.POST["rate"]
    q = request.POST["quantity"]
    cp = int(r)*int(q)
    p = Product.objects.create(name=pn, rate=r, quantity=q, cost_price=cp)
    return HttpResponse("product saved")