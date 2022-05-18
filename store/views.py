from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import RegistrationForm,LoginForm
from django.contrib.auth import authenticate,login,logout
from .models import *
import json
from pprint import pprint

def index(request):
    products = Product.objects.all()
    categories = Category.objects.all().order_by('name')
    return render(request, 'index.html',context={'products':products, 'categories':categories})

def product_by(request):
    data = json.loads(request.body)
    print(data['sort'])
    sort = data['sort']
    if sort=='reyting':
        products = Product.objects.all().order_by('reyting')

    elif sort=='onsale':
        products = Product.objects.filter(quantity__isnull=False)

    pd = [{"id": p.id, "name": p.name, 'image': p.imageURL, 'price': p.price, 'discount': p.with_discount,"category": p.category.name,"reyting": p.reyting} for p in products]

    return JsonResponse({"products":pd})

def product_info(request,id):
    product = Product.objects.get(id=id)
    product_like = Product.objects.filter(category__product=product)
    return render(request, 'product-extended.html', {'product': product,'product_like':product_like})

@login_required(login_url="log_in")
def cart(request):
    return render(request, 'cart.html')

@login_required(login_url="log_in")
def wishlist(request):
    return render(request, 'wishlist.html')

@login_required(login_url="log_in")
def checkout(request):
    return render(request, 'checkout.html')

def category(request,id):
    products_discount = Product.objects.filter(category_id=id,discount__isnull=False)
    products = Product.objects.filter(category_id=id,discount__isnull=True)
    categories = Category.objects.all().order_by('name')
    return render(request, 'category-market.html',{'products':products, 'categories':categories, 'products_discount':products_discount,})

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
        # form = RegistrationForm(request.POST)
        # if form.is_valid():
            # form.save()
        try:
            username = request.POST['username']
            email = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
        except:
            return redirect('register')
        if password2==password1:
            User.objects.create_user(username=username,email=email,password=password1)

            user = authenticate(request,username=username,password=password1)
            if user:
                login(request,user)
                return redirect('index')
    return render(request, 'auth/register.html',{})

def log_out(request):
    logout(request)
    return redirect('log_in')
