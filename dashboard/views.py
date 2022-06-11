import json

from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password

from .decorators import adminonly
from django.http import JsonResponse
from django.shortcuts import render, redirect
from user.models import CustomUser
from django.contrib import messages

from dashboard.forms import Add_category
from store.models import Category,Product

@adminonly
def dashboard(request):
    return render(request,'dashboard/dashboard.html')

@adminonly
def add_product(request):
    if request.method=='POST':
        pass
    products = Product.objects.all().order_by('-id')
    categories = Category.objects.all().order_by('id')
    return render(request, 'dashboard/add_product.html',{'products':products,'categories':categories,'size':[i[0] for i in products.first().choice][1:]})

@adminonly
def add_category(request):
    if request.method =='POST':
        name = request.POST['name']
        image = request.FILES['image']
        Category.objects.create(name=name, image=image)
        return redirect('add_category')
    categories = Category.objects.all().order_by('-id')
    return render(request, 'dashboard/add_category.html',{'categories':categories})

def delete_category(request):
    data = json.loads(request.body)
    id = data['id']
    category = Category.objects.get(id=int(id))
    category.delete()
    return JsonResponse({'status':'ok'})

@adminonly
def edit_category(request,id):
    if request.method=='POST':
        name = request.POST['name']
        image = request.FILES['image']
        category = Category.objects.get(id=id)
        category.name = name
        category.image  = image
        category.save()
        return redirect('add_category')

@adminonly
def users(request):
    if request.method=="POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        phone = request.POST['phone']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password2==password1:
            CustomUser.objects.create_user(username=phone,password=password1,phone_number = phone,first_name=firstname,last_name=lastname,is_verify=True)
            messages.success(request,'Yangi user yaratildi')
        else:
            messages.error(request,'Kiritilgan parol mos kelmadi')
    users = CustomUser.objects.all().order_by('-id')
    return render(request,'dashboard/users.html',{'users':users})

def delete_user(request):
    try:
        data = json.loads(request.body)
        id = data['id']
        user = CustomUser.objects.get(id=int(id))
        user.delete()
        return JsonResponse({'status':'ok'})
    except:
        return JsonResponse({'status': 'no'})

@adminonly
def edit_user(request,id):
    if request.method=='POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        phone = request.POST['phone']
        old_password = request.POST['old_password']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        user = CustomUser.objects.get(id=int(id))

        # Passwordni change qilish
        # if user.check_password(old_password): 1-usul
        # if user.password == make_password(old_password):# 2-usul
        if password2 == password1:
            try:
                user.first_name = firstname
                user.last_name = lastname
                user.phone_number = phone
                user.username = phone
                user.set_password(password1)
                user.save()
            except:
                messages.error(request, 'User malumotlari yangilanmadi')
            messages.success(request, 'Yangilandi')
            return redirect('users')
        messages.error(request, 'Kiritilgan parol mos kelmadi')
        return redirect('users')

