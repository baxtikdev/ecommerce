from django.urls import path
from .views import *

urlpatterns = [
    path('billing_data/',billing_data,name='billing_data')
]