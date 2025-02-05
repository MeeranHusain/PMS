from django.urls import path
from . import views

urlpatterns = [

    path('user/',views.UserProfile.as_view(),name='profile'),
    path('delete-address/<int:id>',views.deleteAddress,name='deleteAddress'),
    path('edit-address/<int:id>',views.editAddress.as_view(),name='editAddress')
    

]