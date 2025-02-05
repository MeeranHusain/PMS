from django import forms
from django.contrib.auth.models import User
from accounts.models import Address,Customer

class UserprofileForm(forms.Form):
    first_name = forms.CharField(max_length=40,widget=forms.TextInput(attrs={'placeholder' : User.username}))
    last_name = forms.CharField(max_length=40)
    username = forms.CharField(max_length=40)
    email = forms.CharField(max_length=30,widget=forms.EmailInput)
    phoneNumber = forms.CharField(max_length=10,widget=forms.NumberInput)
    dob = forms.DateField()