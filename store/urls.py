from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('product_info/',product_info,name='product_info'),
    path('cart/',cart,name='cart'),
    path('wishlist/',wishlist,name='wishlist'),
]