from store.models import Cart_products
from django import template

register = template.Library()

@register.simple_tag
def product_quantity(product_id, user):
    print(product_id,'*************')
    return Cart_products.objects.get(card__user=user,product_id=int(product_id)).quantity