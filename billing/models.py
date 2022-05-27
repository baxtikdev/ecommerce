from django.db import models
from store.models import User,Card,Cart_products

class BillingDetails(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    street_address = models.CharField(max_length=100)
    town = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    postcode = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=15)
    notes = models.TextField(null=True)
    price = models.FloatField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} | {self.country}"
