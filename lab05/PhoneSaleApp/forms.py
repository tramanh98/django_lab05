from .models import Brand, Product
from django.forms import ModelForm
from django import forms


class productForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"


class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = "__all__"
