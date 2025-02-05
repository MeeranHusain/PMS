from django.urls import path
from . import views

urlpatterns = [

    path('payments/',views.procedToPay,name='procedToPay'),
    path('verify_payment/',views.verifyPayment,name='verifyPayment')

]