from django.urls import path, include
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
app_name = 'PhoneSaleApp'
urlpatterns = [
    path('', views.index, name = "index"),
    path('detail/<slug:product_id>', views.detail, name = "detail"),
    path('post/', views.post_product, name = "post"),
    path('update/<slug:product_id>', views.update_product, name = "update")
    # url(r'detail/(?<pk>[^/]+)/$', views.detail, name = "detail")
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
