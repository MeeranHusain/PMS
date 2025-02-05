from django.db import models
from django.contrib.auth.models import User
from products.models import Medicine
from django.core.validators import MinValueValidator
# Create your models here.


class Cart(models.Model):
    # instance = models.Manager()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Medicine,on_delete=models.CASCADE)
    quantity = models.IntegerField(validators =[MinValueValidator(1)])
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = [['user','product']]
    def __str__(self) -> str:
        return self.product.name +' added by ' +self.user.username