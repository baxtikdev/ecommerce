from django.shortcuts import render, redirect
from .forms import RegistrationForm,LoginForm
from django.contrib.auth import authenticate,login,logout
from .models import *

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html',context={'products':products})

def product_info(request):
    return render(request, 'product-extended.html')

def cart(request):
    return render(request, 'cart.html')

def wishlist(request):
    return render(request, 'wishlist.html')

def checkout(request):
    return render(request, 'checkout.html')

def category(request):
    return render(request, 'category-market.html')

def contact(request):
    return render(request, 'contact.html')

def log_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                return redirect('index')
    return render(request, 'auth/login.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                return redirect('index')
    return render(request, 'auth/register.html',{})

def log_out(request):
    logout(request)
    return redirect('log_in')
