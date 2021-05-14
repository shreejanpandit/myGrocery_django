from django.db import models
from apps.category.models import Category
from apps.product.models import Product


# Create your models here.

class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE, max_length=50)
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE, max_length=50)
    quantity = models.IntegerField(blank=True)
    totalPrice = models.FloatField(null=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __int__(self):
        return self.id
