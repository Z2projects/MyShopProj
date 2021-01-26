from django.db import models

# Create your models here.
class ProductType(models.Model):
    ptype = models.CharField(max_length=10, null=True)

class Product(models.Model):
    name = models.CharField(max_length=10,unique=True)
    ptype = models.ForeignKey(ProductType, null=True, blank=True, on_delete=models.CASCADE)

class Buy(models.Model):
    bp = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE)
    bdate = models.DateField()
    brate = models.IntegerField()
    bquantity = models.IntegerField()

class Sell(models.Model):
    sp = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE)
    sdate = models.DateField()
    srate = models.IntegerField()
    squantity = models.IntegerField()