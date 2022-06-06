import json
from django.http import JsonResponse
from django.shortcuts import render, redirect

from dashboard.forms import Add_category
from store.models import Category

def dashboard(request):
    return render(request,'dashboard/dashboard.html')

def add_product(request):
    return render(request, 'dashboard/add_product.html')

def add_category(request):
    if request.method =='POST':
        print(request.POST)
        name = request.POST['name']
        print(name)
        image = request.FILES['image']
        print(image)
        Category.objects.create(name=name, image=image)
        return redirect('add_category')
    categories = Category.objects.all().order_by('-id')
    return render(request, 'dashboard/add_category.html',{'categories':categories})

def delete_category(request):
    data = json.load(request.body)
    id = data['id']
    category = Category.objects.get(id=int(id))
    category.delete()
    return JsonResponse({'status':'ok'})
