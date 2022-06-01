from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('product_by/',product_by,name='product_by'),
    path('product_info/<int:id>/',product_info,name='product_info'),

    #Card
    path('cart/',cart,name='cart'),
    path('add_to_cart/',add_to_cart,name='add_to_cart'),
    path('change_quantity/',change_quantity,name='change_quantity'),
    path('remove_card/',remove_card,name='remove_card'),

    #Wishlist
    path('add_wishlist/',add_wishlist,name='add_wishlist'),
    path('delete_wishlist/',delete_wishlist,name='delete_wishlist'),

    #search
    path('search/',search,name='search'),

    path('wishlist/',wishlist,name='wishlist'),
    path('category/<int:id>/',category,name='category'),
    path('contact/',contact,name='contact'),
    path('checkout/',checkout,name='checkout'),
    path('blog/',blog,name='blog'),
    path('about/',about,name='about'),
]