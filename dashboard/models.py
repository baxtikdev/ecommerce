from django.db import models
from store.models import Product,Category
from user.models import CustomUser

class Shipper(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} | {self.product.name}"

class Recieve_Product(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    shipper = models.ForeignKey(Shipper, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.shipper.user.username} | {self.product.name}"