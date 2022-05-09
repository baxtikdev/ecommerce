from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Color)
admin.site.register(Card)
admin.site.register(Wishlist)
admin.site.register(SaleHistory)
