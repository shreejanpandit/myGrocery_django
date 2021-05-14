from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Setting(models.Model):
    id = models.AutoField(primary_key=True)
    name_of_grocery = models.CharField(max_length=122)
    address = models.CharField(max_length=122)
    email = models.EmailField()
    est_date = models.DateField()
    website = models.URLField()
    facebook = models.URLField()
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, max_length=50)

    def __str__(self):
        return self.name_of_grocery
