from django import template
from django.db.models import Sum
from django.templatetags.static import static

register = template.Library()


@register.simple_tag
def get_price(request, x):
    price = request.GET.get('price')
    if price:
        return price.split(';')[x]
    return 'null'
