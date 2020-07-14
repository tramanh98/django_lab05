from django.shortcuts import render
from ..models import Brand, Product
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.inclusion_tag('./PhoneSaleApp/item.html')
def show_results():
    p = Product.objects.all().order_by("updatedAt").reverse()[:10]
    print(p)
    return {"products": p}


@register.filter(name='color_item',is_safe=True)
def color_item(IDitem):
    if IDitem == 1:
        color = 'pro1'
    elif IDitem == 2:
        color = 'pro2'
    else:
        color = 'other'
    return color