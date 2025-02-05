from django.shortcuts import render,get_object_or_404,redirect
from django.views import View
from . forms import UserprofileForm
from accounts.models import Customer,Address
from accounts.forms import AddressForm
from django.contrib.auth.decorators import login_required

# Create your views here.

class UserProfile(View):
    def get(self,request):
        user = request.user
        loggedCustomer = get_object_or_404(Customer,user=user)

        form = UserprofileForm(initial={
            'first_name': user.first_name,
            'last_name': user.last_name,
            'username': user.username,  
            'email': user.email,
            'phoneNumber': loggedCustomer.phoneNumber,
            'dob': loggedCustomer.dob
        })

        address_list = Address.objects.filter(user = loggedCustomer)

        context = {
            'form': form,
            'addressForm' : AddressForm(),
            'detail' : address_list
        }

        return render(request,'userprofile/user.html',context)

    def post(self,request):
        user = request.user
        customer = get_object_or_404(Customer,user=user)
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = customer
            address.save()
            return redirect('profile')
        else:
            return redirect('index')
        

@login_required
def deleteAddress(request,id):
    address = get_object_or_404(Address,id=id)
    address.delete()
    return redirect('profile')

class editAddress(View):
    def get(self,request,id):
        address = get_object_or_404(Address,id=id)
        if address:
            context = {
                'addressForm' : AddressForm(instance=address)
            }
            return render(request,'userprofile/user.html',context)

    def post(self,request,id):
        user = request.user
        customer = get_object_or_404(Customer,user = user)
        address = get_object_or_404(Address,id=id)
        addressForm = AddressForm(request.POST,instance=address)
        if addressForm.is_valid():
            form = addressForm.save(commit=False)
            form.user = customer
            form.save()
            return redirect('profile')
        else:
            return render(request,'userprofile/user.html',{'addressForm':addressForm})
        