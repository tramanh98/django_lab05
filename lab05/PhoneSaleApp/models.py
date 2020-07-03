from django.db import models
from django.core.validators import MinValueValidator, MinLengthValidator

# Create your models here.


class Brand (models.Model):
    idBrand = models.CharField(unique=True,primary_key=True, validators=[
                               MinLengthValidator(3, message="ID must have at least 3 characters")], max_length=20)
    nameBrand = models.CharField(max_length=200)
    descriptionBrand = models.TextField(default="This is a famous brand")

    def __str__(self):
        return self.idBrand


class Product (models.Model):
    idProduct = models.CharField(unique=True, primary_key=True, max_length=20, validators=[
        MinLengthValidator(3, message="Id must have at least 3 characters")])
    name = models.CharField(max_length=200)
    description = models.TextField(default="This is a product")
    price = models.IntegerField(validators=[MinValueValidator(
        10000, message="The price must bigger than 10000")])
    numberRemain = models.IntegerField()
    createdAt = models.DateTimeField("Time create", auto_now_add=True)
    updatedAt = models.DateTimeField("Time update", auto_now=True)
    avatar = models.ImageField(upload_to="avatar/")
    idBrandProduct = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return self.idProduct
