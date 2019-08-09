from django.urls import path
from .views import GetProducts, GetActiveProducts, DeleteProduct, DisableProduct

urlpatterns = [
    path('get-products/', GetProducts.as_view(), name='get_products'),
    path('get-active-products/', GetActiveProducts.as_view(),
         name='get_active_products'),
    path('delete-product/', DeleteProduct.as_view(), name='delete_product'),
    path('disable-product/', DisableProduct.as_view(), name='disable_product'),
]
