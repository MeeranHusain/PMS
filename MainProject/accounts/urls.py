from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    
    path('forgot-password/',views.ForgotPassword.as_view(),name='forgot_password'), 
    path('verify-otp/',views.verify_otp,name='verify_otp'),
    path('reset-password/',views.reset_password,name='reset_password'),
    
    path('about/',views.about,name='about'),   

]