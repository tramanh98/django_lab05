from django.shortcuts import render
from .models import Brand, Product
from .forms import productForm, BrandForm
from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest

# Create your views here.
# home: output: teen cac brand va 10 san pham moi nhat


def index(request):
    first10Items = Product.objects.all()[:10]
    return render(request, "PhoneSaleApp/index.html", first10Items)

# input: id (param), output: render (request, url, json), JSON: y het model


# chi tiết sản phẩm


def detail(request):
    # idPro = request.query_params.get("idProduct")
    #   check = Product.objects.get(Product.idProduct=idPro)
    #    if check != null:
    return render(request, "PhoneSaleApp/PostProducts.html")
    #     else:
    # return HttpResponseBadRequest("No product, please add")


# đăng tải bài đăng mới


def post_product(request):
    if request.method == "GET":
        return render(request, "PhoneSaleApp/PostProducts.html")
    else:
        return HttpResponseBadRequest("No product, please add")
    if request.method == "POST":
        formProduct = productForm(request.data)
        if formProduct.is_valid():
            formProduct.save()
            return HttpResponse("Success")
        else:
            return HttpResponseBadRequest("Invalid info, please try again")


# post san pham moi: input: model san pham, output: json{success: true}
# update san pham: input: nhu tren, output nhu tren
# delete: input: id (param), output: json{success: true or false}
# list brand: input: idBrand (param), output: json{model Brand}
# Validation: input: model San Pham, check gia, ten
# gia: >10k, must have, int
# ten san pham: must have >=10 char, unique
