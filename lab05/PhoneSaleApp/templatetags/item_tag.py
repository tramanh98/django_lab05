from django.shortcuts import render
from ..models import Brand, Product
from django import template
# Create your views here.
# home: output: teen cac brand va 10 san pham moi nhat

register = template.Library()

@register.inclusion_tag('./PhoneSaleApp/item.html')
def show_results():
    p = Product.objects.all().order_by("updatedAt").reverse()[:10]
    return {"products": p}