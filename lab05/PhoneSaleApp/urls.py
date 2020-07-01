from django.urls import path, include
from . import views

app_name = 'PhoneSaleApp'
urlpatterns = [
    path('', views.index, name = "index"),
    path('detail/', views.detail, name = "prodetail"),
    path('post/', views.postproduct, name = "post")
]