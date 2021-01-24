from django.shortcuts import render
from django.http import HttpResponse
from .models import Buy
from datetime import datetime

# Create your views here.
def buy_product(request):
    return render(request, 'buy_transaction.html')

def buy_save(request):
    pn = request.POST["product_name"]
    t = request.POST["product_type"]
    r = request.POST["rate"]
    q = request.POST["quantity"]
    d = datetime.now()
    Buy.objects.create(name=pn, ptype=t, bdate=d, rate=r, quantity=q)
    return HttpResponse("product saved")

def buy_history(request):
    transactions = Buy.objects.all()
    return render(request, 'buy_history.html', {'txns': transactions})
