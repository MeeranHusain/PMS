from django.urls import path
from . import views

urlpatterns = [
    path('add_to_cart/<int:id>/',views.add_to_cart,name='add_to_cart'),
    path('cart/',views.cart,name = 'cart'),
    path('clear_cart/',views.clear_cart,name = 'clear_cart'),
    path('update_cart/',views.update_cart,name = 'update_cart'),
    path('update_cart/',views.update_cart,name = 'checkout'),
    path('remove-item-from-cart/<int:id>/',views.remove_item_from_cart,name="remove_item_from_cart"),
    # path('add-to-cart/<int:id>/', views.login_redirect, name='add_to_cart_redirect'),  # This handles the login redirection
]