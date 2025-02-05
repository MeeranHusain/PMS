# Create your views here.
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Cart
from products.models import Medicine
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse


# This function is triggered when the user is not logged in
@login_required
def add_to_cart(request, id):
    quantity = int(request.GET.get('quantity',1))
    # print(quantity)
    user = request.user
    product = get_object_or_404(Medicine, id=id)
    
    
    # print(request.GET.get('next'),"here")
    try:
        # Check if the item already exists in the cart
        obj = Cart.objects.get(user=user, product=product)

        # Ensure that adding one more does not exceed stock
        if obj.quantity + quantity <= product.stock:
            obj.quantity += quantity
            obj.save()
        else:
            # If the desired quantity exceeds stock, show a message to the user
            messages.error(request, "Cannot add more than available stock.")
        if '/account/login/' not in (request.META.get('HTTP_REFERER')):  # Redirect back to the same page
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            return redirect(f'/products/product/product/{id}')
    except Cart.DoesNotExist:
        # If the item doesn't exist, create it with quantity 1
        if product.stock >= 1:
            Cart.objects.create(user=user, product=product, quantity=quantity)
        else:
            # Handle the case where there is no stock available
            messages.error(request, "Product out of stock.")
    
    return redirect(request.META.get('HTTP_REFERER'))  # Redirect back to the same page




@login_required 
def cart(request):
    user  = get_object_or_404(User,username=request.user)
    cart = Cart.objects.filter(user = user)
    return render(request,'cart/cart.html',{'cart':cart})




@login_required
def clear_cart(request):
    #request.session['cart_item_count'] = 0
    user  = get_object_or_404(User,username=request.user)
    Cart.objects.filter(user = user).delete()
    return redirect('/carts/cart/')


@login_required
def update_cart(request):
    user = get_object_or_404(User, username=request.user)
    cart = Cart.objects.filter(user=user)
    
    for item in cart:
        # Retrieve the quantity from the POST data
        quantity = request.POST.get(str(item.id))
        
        # Check if the quantity is not None and can be converted to an integer
        if quantity is not None:
            try:
                quantity = int(quantity)
                
                # Check if the requested quantity is less than 1, remove the item if so
                if quantity < 1:
                    item.delete()
                # Check if the requested quantity exceeds available stock
                elif quantity <= item.product.stock:
                    # Update item quantity
                    item.quantity = quantity
                    item.save()
                else:
                    # If the requested quantity exceeds available stock, show a message
                    available_stock = item.product.stock
                    messages.error(
                        request, 
                        f"Product '{item.product.name}' is only {available_stock} available in stock."
                    )
            except ValueError:
                # Handle cases where the quantity is not a valid integer
                continue
        else:
            # If no valid quantity is provided, continue without changes
            continue

    return redirect('cart')





@login_required    
def remove_item_from_cart(request,id):
    Cart.objects.get(id = id).delete()
    #request.session['cart_item_count'] -=1
    return redirect('cart')