from django import forms

from .models import Customer,Address
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User



class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password'] 
        field_order = ['first_name','last_name','username','email','password','confirm_password',] # add other necessary fields here
        widgets = {
            'dob': forms.TextInput(attrs={'class': 'form-control', 'id': 'id_dob'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password:
            if password != confirm_password:
                raise forms.ValidationError("Passwords do not match.")
        return cleaned_data


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ['user']


# forms.py
class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['title', 'block_number', 'building', 'street', 'land_mark', 'area', 'pincode', 'city','state']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'e.g, Home, Work', 'class': 'form-control'}),
            'block_number': forms.TextInput(attrs={'placeholder': 'Enter block_number', 'class': 'form-control'}),
            'building': forms.TextInput(attrs={'placeholder': 'Enter building', 'class': 'form-control'}),
            'street': forms.TextInput(attrs={'placeholder': 'Enter street', 'class': 'form-control'}),
            'land_mark': forms.TextInput(attrs={'placeholder': 'Enter land_mark', 'class': 'form-control'}),
            'area': forms.TextInput(attrs={'placeholder': 'Enter area', 'class': 'form-control'}),
            'city': forms.TextInput(attrs={'placeholder': 'Enter city', 'class': 'form-control'}),
            'pincode': forms.NumberInput(attrs={'placeholder': 'Enter pincode', 'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-select'}),
        }



class ForgetPasswordForm(forms.Form):
    username = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'placeholder':'Enter username','class':'form-control'}))
    email = forms.CharField(max_length=50,widget=forms.EmailInput(attrs={'placeholder':'name@example.com','class':'form-control'}))




class OTPForm(forms.Form):
    otp = forms.IntegerField(max_value=9999,min_value=1000,widget=forms.NumberInput(attrs={'placeholder':'Enter 4-digit otp','class':'form-control'}))



class ResetPasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter new password','class':'form-control'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm new password','class':'form-control'}))
    
    # def clean(self):
    #     cleaned_data = super().clean()
    #     password = cleaned_data.get('password')
    #     confirm_password = cleaned_data.get('confirm_password')

    #     if password and confirm_password:
    #         if password != confirm_password:
    #             raise forms.ValidationError("Passwords do not match.")
    #     return cleaned_data
