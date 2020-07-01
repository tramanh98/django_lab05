from django.shortcuts import render
from .models import Brand, Product
from .forms import productForm, BrandForm
from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest

# Create your views here.
# home: output: teen cac brand va 10 san pham moi nhat


def index(request):
    return render(request, "PhoneSaleApp/index.html")

# input: id (param), output: render (request, url, json), JSON: y het model


def detail(request):
    return render(request, "PhoneSaleApp/ProductDetail.html")

# post san pham moi: input: model san pham, output: json{success: true}
# update san pham: input: nhu tren, output nhu tren
# delete: input: id (param), output: json{success: true or false}
# list brand: input: idBrand (param), output: json{model Brand}
# Validation: input: model San Pham, check gia, ten
# gia: >10k, must have, int
# ten san pham: must have >=10 char, unique
