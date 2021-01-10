from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=10)
    rate = models.IntegerField()
    quantity = models.IntegerField()
    cost_price = models.IntegerField()
