from .models import Cart
from django.contrib.auth.models import User

def cart_items(request):
    if request.user.is_authenticated:
        user = User.objects.get(username = request.user)
        count =Cart.objects.filter(user = user).count() 
        request.session['cart_item_count'] = count
        return dict()
    return dict()