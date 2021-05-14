from django.forms import ModelForm
from .models import Product


class UpdateProduct(ModelForm):
    class Meta:
        model = Product
        fields = (
            'name', 'totalScale', 'unitPrice', 'buyPrice', 'msrp', 'productCode', 'quantityInScale', 'quantityInStock',
            'totalPrice')
