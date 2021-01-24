from django.shortcuts import render
from .models import Product
from .models import PType
from django.http import HttpResponse
import json

# Create your views here.
def product_entry(request):
    p = PType.objects.all()
    return render(request, 'product_entry.html', {'ptypes': p})

def product_list(request):
    p = Product.objects.all()
    return render(request, 'product_list.html', {'products': p})

def product_save(request):
    pn = request.POST["product_name"]
    t = PType.objects.get(ptype=request.POST["product_type"])
    r = request.POST["rate"]
    q = request.POST["quantity"]
    try:
        Product.objects.get(name=pn)
        return HttpResponse("product already exists - no updates made - review code")
    except Product.DoesNotExist:
        Product.objects.create(name=pn, ptype=t, rate=r, quantity=q)
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
        data = {'name': res.name, 'prod_type': res.ptype, 'rate': res.rate, 'quantity': res.quantity}
        return HttpResponse(json.dumps(data))
    except Product.DoesNotExist:
        return HttpResponse("product does not exist")

def product_type_entry(request):
    return render(request, 'product_type_entry.html')

def product_type_save(request):
    t = request.POST["product_type"]
    try:
        PType.objects.get(ptype=t)
        return HttpResponse("product type already exists")
    except PType.DoesNotExist:
        PType.objects.create(ptype=t)
        return HttpResponse("new product type saved")

def product_type_list(request):
    p = PType.objects.all()
    return render(request, 'product_type_list.html', {'ptypes': p})