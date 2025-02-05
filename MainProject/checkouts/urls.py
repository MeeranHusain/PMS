from django.urls import path
from . import views

urlpatterns = [

    path('checkout/',views.Checkout.as_view(),name='checkout'),
    path('select/<int:id>/',views.select_address,name='select_address'),
    
]