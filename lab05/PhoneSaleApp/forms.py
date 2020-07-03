from .models import Brand, Product
from django.forms import ModelForm
from django import forms


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['idProduct','name','description','price','numberRemain','idBrandProduct','avatar']
        widgets = {
            'idProduct': forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Nhập mã sản phẩm' }),
            'name' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Nhập tên sản phẩm', }),
            'description' : forms.Textarea(attrs={'rows':10 ,'class': 'form-control'}),
            'price' : forms.NumberInput(attrs={'class': 'form-control', 'placeholder' : 'Nhập giá bán'}),
            'numberRemain' : forms.NumberInput(attrs={'class': 'form-control', 'placeholder' : 'Số lượng sản phẩm'}),
            'idBrandProduct' : forms.Select(attrs={'class': 'form-control'}),
            'avatar' : forms.FileInput(attrs={'class': 'form-control-file'}),
        }


class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = "__all__"
