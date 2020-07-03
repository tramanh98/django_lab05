# Generated by Django 3.0.4 on 2020-07-01 18:37

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idBrand', models.CharField(max_length=20, unique=True, validators=[django.core.validators.MinLengthValidator(3, message='ID must have at least 3 characters')])),
                ('nameBrand', models.CharField(max_length=200)),
                ('descriptionBrand', models.TextField(default='This is a famous brand')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idProduct', models.CharField(max_length=20, unique=True, validators=[django.core.validators.MinLengthValidator(3, message='Id must have at least 3 characters')])),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(default='This is a product')),
                ('price', models.IntegerField(validators=[django.core.validators.MinValueValidator(10000, message='The price must bigger than 10000')])),
                ('numberRemain', models.IntegerField()),
                ('createdAt', models.DateTimeField(auto_now_add=True, verbose_name='Time create')),
                ('updatedAt', models.DateTimeField(auto_now=True, verbose_name='Time update')),
                ('avatar', models.ImageField(upload_to='avatar/')),
                ('idBrandProduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PhoneSaleApp.Brand')),
            ],
        ),
    ]
