from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

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
    return render(request, 'auth/login.html')
