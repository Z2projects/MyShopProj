from django.db import models

# Create your models here.
class PType(models.Model):
    ptype = models.CharField(max_length=10, null=True)

class Product(models.Model):
    name = models.CharField(max_length=10,unique=True)
    ptype = models.ForeignKey(PType, null=True, blank=True, on_delete=models.CASCADE)
    rate = models.IntegerField()
    quantity = models.IntegerField()