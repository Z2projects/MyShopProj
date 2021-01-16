from django.shortcuts import render
from .models import Product
from django.http import HttpResponse
import json

# Create your views here.
def product_entry(request):
    return render(request, 'product_entry.html')

def product_list(request):
    p = Product.objects.all()
    return render(request, 'product_list.html', {'products': p})

def product_save(request):
    pn = request.POST["product_name"]
    t = request.POST["product_type"]
    r = request.POST["rate"]
    q = request.POST["quantity"]
    cp = int(r)*int(q)
    p = Product.objects.create(name=pn, ptype=t, rate=r, quantity=q, cost_price=cp)
    return HttpResponse("product saved")

def product_delete(request):
    return render(request, 'product_delete.html')

def product_deleted(request):
    Product.objects.filter(name=request.POST["product_name"]).delete()
    return HttpResponse("product removed")

def product_search(request):
    return render(request, 'product_search.html')

def product_detail(request):
    try:
        res = Product.objects.get(name=request.POST["product_name"])
        data = {'name': res.name, 'prod_type': res.ptype, 'rate': res.rate, 'quantity': res.quantity, 'cost_price': res.cost_price}
        return HttpResponse(json.dumps(data))
    except Product.DoesNotExist:
        return HttpResponse("product does not exist")
