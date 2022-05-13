from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('product_info/',product_info,name='product_info'),
    path('cart/',cart,name='cart'),
    path('wishlist/',wishlist,name='wishlist'),
    path('category/',category,name='category'),
    path('contact/',contact,name='contact'),
    path('checkout/',checkout,name='checkout'),

    #Auth
    path('log_in/',log_in,name='log_in'),
]