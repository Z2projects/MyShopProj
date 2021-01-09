from django.db import models

# Create your models here.

class Purchase(models.Model):
    product_name = models.CharField(max_length=30)
    cost_price = models.DecimalField(decimal_places=2,max_digits=10)
    quantity = models.IntegerField()
