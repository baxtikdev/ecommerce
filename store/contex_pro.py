from .models import Card,Category

def context_process(request):
    print(request.user)
    try:
        products = Card.objects.get(user=request.user).product.all()
        context = {
            'categories': Category.objects.all(),
            'products': products,
            'total': sum(products.values_list('price',flat=True))
        }
    except:
        context = {
            'categories': Category.objects.all(),
        }
    return context