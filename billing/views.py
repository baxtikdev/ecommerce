from django.shortcuts import render

from user.models import CustomUser
from .models import *

def billing_data(request):
    if request.method=="POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        street = request.POST['street']
        city = request.POST['city']
        country = request.POST['country']
        postcode = request.POST['postcode']
        phone = request.POST['phone']
        email = request.POST['email']
        try:
            note = request.POST['note']
        except:
            note = 'Note'
        print(request.user)
        user = CustomUser.objects.get(username=request.user.username)
        price = Card.objects.get(user_id=user.id).total_price
        BillingDetails.objects.create(user=request.user, first_name=firstname,last_name=lastname,street_address=street,town=city,country=country,postcode=postcode,phone=phone,email=email,notes=note,price=price)
        if not user.first_name:
            user.first_name = firstname
            user.last_name = lastname
            user.email = email
            user.save()

    return render(request,'billing/card_number.html')
