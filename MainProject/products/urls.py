from django.urls import path
from . import views

urlpatterns = [
    # URL for the "all products" page (may also show bikes depending on the filter).
    path('all-products/', views.all_medicine, name='all_products'),
    path('products/product/<int:product_id>/', views.product_detail, name='product'),
    # path('products/product/<int:product_id>/', views.product_detail, name='add_to_cart'),
    path('search/', views.search_product, name='search_product'),
]