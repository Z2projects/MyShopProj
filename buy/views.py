from django.shortcuts import render
from django.http import HttpResponse
from .models import ProductType
from .models import Product
from .models import Buy
from .models import Sell
from django.http import JsonResponse

# Create your views here.
def product_type_form(request):
    return render(request, 'product_type_entry.html')

def product_type_save(request):
    t = request.POST["product_type"]
    try:
        ProductType.objects.get(ptype=t)
        return HttpResponse("product type already exists")
    except ProductType.DoesNotExist:
        ProductType.objects.create(ptype=t)
        return HttpResponse("new product type saved")

def product_type_list(request):
    p = ProductType.objects.all()
    return render(request, 'product_type_list.html', {'ptypes': p})

def product_form(request):
    p = ProductType.objects.all()
    return render(request, 'product_entry.html', {'ptypes': p})

def product_save(request):
    t = ProductType.objects.get(ptype=request.POST["product_type"])
    p = request.POST["product_name"]
    try:
        Product.objects.get(name=p)    
        return HttpResponse("product already exists")
    except Product.DoesNotExist:
        Product.objects.create(name=p,ptype=t)
        return HttpResponse("new product saved")

def product_list(request):
    p = Product.objects.all()
    return render(request, 'product_list.html', {'products': p})

def buy_product_form(request):
    p = Product.objects.all()
    pt = ProductType.objects.all()
    return render(request, 'buy_transaction.html', {'products': p, 'producttypes': pt})

def buy_product(request):
    p = Product.objects.get(name=request.POST["product_name"])
    r = request.POST["rate"]
    q = request.POST["quantity"]
    uq = p.quantity + int(q)
    Product.objects.filter(name=request.POST["product_name"]).update(quantity=uq)
    Buy.objects.create(bp=p,brate=r,bquantity=q)
    return HttpResponse("buy transaction saved")

def buy_history(request):
    b = Buy.objects.all()
    return render(request, 'buy_history.html', {'allbuy': b})

def sell_product_form(request):
    p = Product.objects.all()
    pt = ProductType.objects.all()
    return render(request, 'sell_transaction.html', {'products': p, 'producttypes': pt})
        
def sell_product(request):
    p = Product.objects.get(name=request.POST["product_name"])
    r = request.POST["rate"]
    q = request.POST["quantity"]
    if p.quantity >= int(q):
        uq = p.quantity - int(q)
        Product.objects.filter(name=request.POST["product_name"]).update(quantity=uq)
        Sell.objects.create(sp=p,srate=r,squantity=q)
        return HttpResponse("sell transaction saved")
    else:
        return HttpResponse("no stock for this product")

def sell_history(request):
    s = Sell.objects.all()
    return render(request, 'sell_history.html', {'allsell': s})

def get_json_product_data(request, *args, **kwargs):
    selected_type = kwargs.get('pt')
    obj_product = list(ProductType.objects.get(ptype=selected_type).product_set.all().values())
    return JsonResponse({'data':obj_product})