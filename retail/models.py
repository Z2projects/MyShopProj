from django.db import models
from datetime import datetime

class ProductType(models.Model):
    ptype = models.CharField(max_length=10, unique=True)

class Product(models.Model):
    name = models.CharField(max_length=10, unique=True)
    ptype = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

class Buy(models.Model):
    bp = models.ForeignKey(Product, on_delete=models.CASCADE)
    bdate = models.DateTimeField(default=datetime.now)
    brate = models.IntegerField()
    bquantity = models.IntegerField()

class Sell(models.Model):
    sp = models.ForeignKey(Product, on_delete=models.CASCADE)
    sdate = models.DateTimeField(default=datetime.now)
    srate = models.IntegerField()
    squantity = models.IntegerField()
