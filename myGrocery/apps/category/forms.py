from django.forms import ModelForm
from .models import Category


class UpdateCategory(ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'remarks')
