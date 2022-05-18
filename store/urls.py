from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('product_by/',product_by,name='product_by'),
    path('product_info/<int:id>/',product_info,name='product_info'),
    path('cart/',cart,name='cart'),
    path('wishlist/',wishlist,name='wishlist'),
    path('category/<int:id>/',category,name='category'),
    path('contact/',contact,name='contact'),
    path('checkout/',checkout,name='checkout'),

    #Auth
    path('log_in/',log_in,name='log_in'),
    path('register/',register,name='register'),
    path('log_out/',log_out,name='log_out'),
]