from .models import Card,Category

def context_process(request):
    products = Card.objects.get(user=request.user).product.all()
    context = {
        'categories': Category.objects.all(),
        'products': products,
        'total': sum(products.values_list('price',flat=True))
    }
    return context