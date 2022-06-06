from django.urls import path
from .views import *

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('add_category/', add_category, name='add_category'),
    path('delete_category/', delete_category, name='delete_category'),
    path('add_product/', add_product, name='add_product')
]