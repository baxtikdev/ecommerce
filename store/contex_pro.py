from .models import Card,Category,Cart_products

def context_process(request):
    try:
        products = Card.objects.get(user=request.user).product.all()
        context = {
            'categories': Category.objects.all(),
            'card_products': products,
            'total': sum(Cart_products.objects.filter(card__user=request.user).values_list('total',flat=True)),
            'count':products.count()
        }
    except:
        context = {
            'categories': Category.objects.all(),
        }
    return context