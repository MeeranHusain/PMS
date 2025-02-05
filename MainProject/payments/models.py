from django.db import models
from django.contrib.auth.models import User
from orders.models import Order

# Create your models here.

STATUS_CHOICE = [
    ('PENDING','PENDING'),
    ('COMPLETED','COMPLETED'),
    ('FAILED','FAILED'),
]

METHOD_CHOICE =[
    ('UPI','UPI'),
    ('COD','COD'),
    ('RAZORPAY','RAZORPAY'),
]

class Payment(models.Model):
    
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    razorpay_orderId = models.CharField(max_length=25,blank=True)
    razorpay_paymentId = models.CharField(max_length=25,blank=True)
    payment_signature = models.CharField(max_length=128,blank=True)
    amount = models.DecimalField(decimal_places=2,max_digits=12)
    status = models.CharField(choices=STATUS_CHOICE,max_length=20)
    method = models.CharField(choices=METHOD_CHOICE,max_length=20)
    order = models.ForeignKey(Order,on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.user.username}'