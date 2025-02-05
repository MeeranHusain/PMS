from django.shortcuts import render, redirect, get_object_or_404
from carts.models import Cart
from carts.views import cart
from django.views import View
from accounts.forms import AddressForm
from accounts.models import Address, Customer
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.http import JsonResponse


class Checkout(View):
    def get(self, request):
        user = request.user
        user = get_object_or_404(User, username=user)
        customer = get_object_or_404(Customer, user=user)
        customerAddress = Address.objects.filter(user=customer)
        cartProduct = Cart.objects.filter(user=user)
        cart_item = cartProduct.count()
        addressForm = AddressForm()
        subtotal = sum(item.product.price * item.quantity for item in cartProduct)
        shipping_cost = 50
        total = subtotal + shipping_cost 

        # Render the template with context data
        context = {
            'address': addressForm,
            'data': cartProduct,
            'displayAddress': customerAddress,
            'cartCount': cart_item,
            'subtotal': subtotal,
            'shipping_cost': shipping_cost,
            'total': total,
        }
        return render(request, 'checkout/checkout.html', context)
    
    def post(self, request):
        addressForm = AddressForm(request.POST)
        if addressForm.is_valid():
            customer = Customer.objects.get(user=request.user)

            address = Address.objects.create(
                user=customer,
                title=addressForm.cleaned_data['title'],
                block_number=addressForm.cleaned_data['block_number'],
                building=addressForm.cleaned_data['building'],
                street=addressForm.cleaned_data['street'],
                land_mark=addressForm.cleaned_data['land_mark'],
                area=addressForm.cleaned_data['area'],                
                city=addressForm.cleaned_data['city'],
                state=addressForm.cleaned_data['state'],
                pincode=addressForm.cleaned_data['pincode'],
                
                # address_line_1=addressForm.cleaned_data['address_line_1'],
                # address_line_2=addressForm.cleaned_data['address_line_2'],
            )
            address.save()

            return redirect('checkout')  # Redirect back to checkout after adding address

@login_required
def select_address(request, id):
    selected_address = get_object_or_404(Address, id=id, user=request.user.customer)
    Address.objects.filter(user=request.user.customer, is_selected=True).update(is_selected=False)

    # Set the selected address to is_selected=True
    selected_address.is_selected = True
    selected_address.save()

    return redirect('checkout')