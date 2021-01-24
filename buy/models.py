from django.db import models

# Create your models here.
class Buy(models.Model):
    name = models.CharField(max_length=10)
    ptype = models.CharField(max_length=10)
    bdate = models.DateField()
    rate = models.IntegerField()
    quantity = models.IntegerField()
