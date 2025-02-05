from django.shortcuts import get_object_or_404,redirect,HttpResponse
from accounts.models import Customer,Address
from carts.models import Cart 
from orders.models import Order

import razorpay
from razorpay import Client
from django.conf import settings

from payments.models import Payment
from json import dumps
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.timezone import localtime
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
# Create your views here.
from json import dump

@login_required
def procedToPay(request):
    try: 
        user = request.user
        user = get_object_or_404(User,username = user)
        userCart = Cart.objects.filter(user = user)
        shipping_cost = 50

        # get the total amount to be paid 
        amount = 0
        subtotal = sum(item.product.price * item.quantity for item in userCart)
        amount = subtotal + shipping_cost
        # amount *= 100
        amount = int(amount)

        # fetch the customer and the address 
        customer = get_object_or_404(Customer, user = user)
        address = Address.objects.filter(user = customer).filter(is_selected=True)[0]
        # print("\n\n\n\n\n\n Hello\n\n\n\n\n\n\n")
        # check if the order is already created or create a new
        order = Order.objects.filter(user = user).filter(status__icontains='CREATED').first()
        if not order:
            order = Order.objects.create(
                user = user,
                customer = customer,
                status = "CREATED",
                order_time = localtime(timezone.now()).time(),
                total = amount,
                shipping_address = address,
            )
            
        # client = Client(auth=("your_key_id", "your_key_secret"))
        
        # create new razorpay user 
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
        # print(client) # client object created 
        data = {"amount" : amount*100 , "currency" : "INR" , "receipt" : str(order.order_uuid)}
        # print(type(data['amount']))
        payment = client.order.create(data=data)
        # print(payment)
        
        context = {
            'RAZORPAY_KEY_ID' : settings.RAZORPAY_KEY_ID,
            'payment' : payment,
            'amount':amount/100,
            'call_back' : '/payment/verify_payment/'
        }
        
        # print("\n\n\n\n\n\n Hello\n\n\n\n\n\n\n")
        
        Payment.objects.create(
            user = user,
            razorpay_orderId = payment['id'],
            amount = amount,
            status = "PENDING",
            method = "RAZORPAY",
            order = order
        )
        # print(HttpResponse(context),context,'here ia m')
        data = dumps(context,indent=4)
        return HttpResponse(data)

    except Exception as e:
        print(e)
        return redirect('home')    
        

       
from orders.models import OrderDetails
from django.views.decorators.csrf import csrf_exempt

from django.contrib import messages

@csrf_exempt  # Exempt from CSRF protection for Razorpay callbacks
def verifyPayment(request):
    print("\n\n\n\n\n\n Hello\n\n\n\n\n\n\n")
    if request.method == "POST":
        try:
            # Fetch the current user from request
            
            user = request.user
            user = get_object_or_404(User, username=user)
            customer = get_object_or_404(Customer, user=user)

            # Initialize Razorpay client
            client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
            
            # print("\n\n\n\n\n\n Hello\n\n\n\n\n\n\n")
            
            # Verify the payment signature sent by Razorpay
            client.utility.verify_payment_signature({
                'razorpay_order_id': request.POST.get('razorpay_order_id'),
                'razorpay_payment_id': request.POST.get('razorpay_payment_id'),
                'razorpay_signature': request.POST.get('razorpay_signature')
            })

            # Get the payment object based on Razorpay order ID
            payment_obj = Payment.objects.get(razorpay_orderId=str(request.POST.get('razorpay_order_id')))
            order = payment_obj.order  # The order linked to the payment

            # Update the payment object with the payment ID and signature
            payment_obj.razorpay_paymentId = str(request.POST.get('razorpay_payment_id'))
            payment_obj.payment_signature = str(request.POST.get('razorpay_signature'))
            payment_obj.status = "COMPLETED"
            payment_obj.save()

            # Update the order status to 'PROCESSING'
            order.status = "PROCESSING"
            order.save()

            # Create order details for each item in the cart
            cart_items = Cart.objects.filter(user=payment_obj.user)
            for item in cart_items:
                OrderDetails.objects.create(
                    order=order,
                    product=item.product,
                    customer=customer,
                    quantity=item.quantity,
                    price=item.product.price
                )
                item.product.stock -= item.quantity
                item.product.save()

            # Send confirmation email to the user
            send_mail(
                subject="Your order has been confirmed!",
                message=f"Dear {user.username}, your order has been confirmed and is being processed.",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user.email],
                fail_silently=True
            )

            # Send an email to the admin notifying them of the new order
            send_mail(
                subject="New order placed!",
                message=f"A new order has been placed by {user.username}.",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.ADMIN_EMAIL],
                fail_silently=True
            )

            # Clear the user's cart after successful payment
            cart_items.delete()

            # Add a success message to be displayed in the template
            messages.success(request, "Thank you for shopping with us!")

            # Redirect to the orders page
            return redirect('orders')  # Ensure the URL name 'orders' is defined in your urls.py

        except Exception as e:
            # Handle any errors that occur during the payment verification
            print(f"Payment verification failed: {e}")
            return redirect('cart')  # Redirect back to the cart if payment verification fails

    else:
        return redirect('cart')