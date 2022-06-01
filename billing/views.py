from django.shortcuts import render
from .models import *

def billing_data(request):
    if request.method=="POST":
        firstname = request.POST['firstname']
    return render(request,'billing/card_number.html')
