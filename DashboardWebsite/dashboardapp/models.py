from django.db import models

# Create your models here.

class Products(models.Model):
    title = models.CharField(max_length=1000)
    price = models.FloatField()
    category = models.CharField(max_length=1000)