from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ProductType
from .models import Product
from .models import Buy
from .models import Sell
from django.http import JsonResponse

def buy_product_form(request):
    pt = ProductType.objects.all()
    return render(request, 'buy_transaction.html', {'producttypes': pt})

def buy_product(request):
    p = Product.objects.get(name=request.POST['product_name'])
    fc = request.POST['from_customer']
    r = request.POST['rate']
    q = request.POST['quantity']
    uq = p.quantity + int(q)
    Product.objects.filter(name=request.POST['product_name']).update(quantity=uq)
    Buy.objects.create(bp=p,from_customer=fc,brate=r,bquantity=q)
    res = p.name + ' of type ' + p.ptype.ptype + ' purchased from customer ' + fc
    return render(request,'results.html', {'result': res})

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

def product_delete_form(request):
    pt = ProductType.objects.all()
    return render(request, 'product_delete.html', {'producttypes': pt})

def product_delete(request):
    p = request.POST['product_name']
    pt = ProductType.objects.filter(ptype=request.POST['product_type'])
    Product.objects.filter(name=p,ptype=pt[0].id).delete()
    return redirect('/retail/')

def product_type_delete_form(request):
    pt = ProductType.objects.all()
    return render(request, 'product_type_delete.html', {'producttypes': pt})

def product_type_delete(request):
    ProductType.objects.filter(ptype=request.POST['product_type']).delete()
    return redirect('/retail/listproducttypes')

def buy_history(request):
    b = Buy.objects.all()
    return render(request, 'buy_history.html', {'allbuy': b})

def sell_product_form(request):
    p = Product.objects.all()
    pt = ProductType.objects.all()
    return render(request, 'sell_transaction.html', {'products': p, 'producttypes': pt})
        
def sell_product(request):
    p = Product.objects.get(name=request.POST["product_name"])
    tc = request.POST["to_customer"]
    r = request.POST["rate"]
    q = request.POST["quantity"]
    dt = request.POST["discount_type"]
    d = request.POST["discount"]
    if p.quantity >= int(q):
        if dt == 'none' or dt == 'flat':
            uq = p.quantity - int(q)
            sell_price = float(r) * int(q)
            discounted_sell_price = sell_price - float(d)
            Product.objects.filter(name=request.POST["product_name"]).update(quantity=uq)
            Sell.objects.create(sp=p,to_customer=tc,srate=r,squantity=q,discounttype=dt,discount=d,sprice=discounted_sell_price)
            return redirect('/retail/sellhistory')
        elif dt == 'percent':
            if float(d) > 0 and float(d) < 100:
                uq = p.quantity - int(q)
                sell_price = float(r) * int(q)
                pd = (float(d)/100) * sell_price
                discounted_sell_price = sell_price - pd
                Product.objects.filter(name=request.POST["product_name"]).update(quantity=uq)
                Sell.objects.create(sp=p,to_customer=tc,srate=r,squantity=q,discounttype=dt,discount=d,sprice=discounted_sell_price)
                return redirect('/retail/sellhistory')
            else:
                return HttpResponse("sell transaction failed - ivalid percentage")
    else:
        return HttpResponse("no stock for the product")

def sell_history(request):
    s = Sell.objects.all()
    return render(request, 'sell_history.html', {'allsell': s})

def get_json_product_data(request, *args, **kwargs):
    selected_type = kwargs.get('pt')
    obj_product = list(ProductType.objects.get(ptype=selected_type).product_set.all().values())
    return JsonResponse({'data':obj_product})

def index(request):
    return render(request, 'index.html')
