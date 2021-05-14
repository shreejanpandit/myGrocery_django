from django.forms import ModelForm
from django.contrib.auth.models import User


class UpdateUser(ModelForm):
    class Meta:
        model = User
        fields = ('first_name','email','address','contact','img')

