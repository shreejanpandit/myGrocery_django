from django.db import models
from apps.category.models import Category


# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=122)
    categoryID = models.ForeignKey(Category, null=True, on_delete=models.CASCADE, max_length=50)
    totalScale = models.IntegerField()
    unitPrice = models.FloatField()
    buyPrice = models.FloatField()
    msrp = models.FloatField()
    totalPrice = models.FloatField()
    productCode = models.CharField(max_length=50)
    quantityInScale = models.IntegerField()
    quantityInStock = models.IntegerField()
    description = models.CharField(max_length=122)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


