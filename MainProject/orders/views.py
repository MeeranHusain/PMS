from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from orders.models import Order

@login_required
def user_orders(request):
    # Retrieve the orders for the currently logged-in user, ordered by the most recent
    orders = Order.objects.filter(user=request.user).order_by('-order_on','-order_time')

    # Pass the orders to the template context
    context = {
        'orders': orders
    }
    
    return render(request, 'order/order.html', context)