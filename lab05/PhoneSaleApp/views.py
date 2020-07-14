from django.shortcuts import get_object_or_404, render
from .models import Product, Brand
from .forms import ProductForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
brand = [
    {
        'name': 'vst',
    }
]

def index(request):
    return render(request, "PhoneSaleApp/index.html")

# input: id (param), output: render (request, url, json), JSON: y het model

# chi tiết sản phẩm
def detail(request, product_id):
    pro = Product.objects.get(idProduct = product_id)
    return render(request, "PhoneSaleApp/ProductDetail.html", {"product": pro})

# đăng tải bài đăng mới
def post_product(request):
    if request.method == "GET":
        form = ProductForm()
        context = {"edit": False, "title": "Đăng sản phẩm mới", "button": "Đăng tin"}
        return render(request, "PhoneSaleApp/PostProducts.html", context )
    if request.method == "POST":
        data = {
         "idProduct": request.POST['idProduct'] ,
         "name": request.POST['name'] ,
         "description": request.POST['description'],
         "price": request.POST['price'],
         "numberRemain": request.POST['numberRemain'],
         "avatar": request.FILES['avatar']}
        idBrandProduct = Brand.objects.get(pk=request.POST['brand'])
        pro = Product.objects.create(**data, idBrandProduct = idBrandProduct )
        return render(request, "PhoneSaleApp/index.html")

# update bài đăng
def update_product(request, product_id):
    pro = Product.objects.get(idProduct = product_id)
    if request.method == "GET":
        content = {"edit": True, "title": "Chỉnh sửa bài đăng", "button": "Cập nhập", "product": pro} 
        return render(request, "PhoneSaleApp/PostProducts.html", content)
    if request.method == "POST":
        pro.name = request.POST['name'] 
        pro.description = request.POST['description']
        pro.price = request.POST['price']
        pro.numberRemain = request.POST['numberRemain']
        pro.avatar = request.FILES['avatar']
        pro.idBrandProduct = Brand.objects.get(pk=request.POST['brand'])
        pro.save()
        return render(request, "PhoneSaleApp/index.html")

@csrf_exempt
def delete_product(request, product_id):
    pro = Product.objects.get(idProduct = product_id)
    if request.method == "DELETE":
        pro.delete()
        return JsonResponse({"message":'success'})


# post san pham moi: input: model san pham, output: json{success: true}
# update san pham: input: nhu tren, output nhu tren
# delete: input: id (param), output: json{success: true or false}
# list brand: input: idBrand (param), output: json{model Brand}
# Validation: input: model San Pham, check gia, ten
# gia: >10k, must have, int
# ten san pham: must have >=10 char, unique
