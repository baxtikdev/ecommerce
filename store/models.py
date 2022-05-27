from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='Category',null=True, blank=True)

    @property
    def imageURL(self):
        try:
            return self.image.url
        except:
            pass

    def __str__(self):
        return self.name

class Color(models.Model):
    name = models.CharField(max_length=20)
    # color_code = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Product(models.Model):
    choice = (
        ('Select a size','Select a size'),
        ('Small','Small'),
        ('Medium','Medium'),
        ('Large','Large'),
        ('Extra large','Extra large'),
    )
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.ImageField(upload_to='Product')
    description = models.TextField()
    color = models.ManyToManyField(Color)
    size = models.CharField(max_length=30,choices=choice,null=True,blank=True)
    quantity = models.IntegerField(default=0)
    reyting = models.FloatField(default=0)
    discount = models.FloatField(default=0,null=True,blank=True)

    @property
    def with_discount(self):
        if self.discount:
            return self.price*(1 - self.discount / 100)
        return self.price

    @property
    def imageURL(self):
        try:
            return self.image.url
        except:
            pass

    def __str__(self):
        return self.name

class Card(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ManyToManyField(Product,null=True,blank=True)
    total_price = models.FloatField(default=0)

    @property
    def total(self):
        self.total_price = sum([i.summa for i in Cart_products.objects.all()])
        self.save()
        return self.total_price

    def __str__(self):
        return f"{self.user.username} | {self.total_price}"

class Cart_products(models.Model):
    card = models.ForeignKey(Card,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    total = models.FloatField(default=0)

    @property
    def summa(self):
        self.total = self.quantity * self.product.price*(1 - self.product.discount/100)
        self.save()
        return self.total


    @property
    def add(self):
        print('ADD',self.quantity)
        self.quantity = self.quantity + 1
        self.save()
        print(self.quantity)
        return self.quantity

    @property
    def sub(self):
        self.quantity = self.quantity - 1
        self.save()
        return self.quantity

    def __str__(self):
        return f"{self.card.user.username} | {self.product.name} | {self.total}"

class Wishlist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)


    def __str__(self):
        return f"{self.id} | {self.user.username}"

class SaleHistory(models.Model):
    payment = (
        ('Humo', 'Humo'),
        ('UzCard', 'UzCard'),
    )

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ManyToManyField(Product)
    payment_type = models.CharField(max_length=20,choices=payment)
    total_price = models.FloatField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} | {self.user.username} | {self.time}"
