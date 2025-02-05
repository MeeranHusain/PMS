from django.contrib import admin
from .models import Order,OrderDetails

# Register your models here.
admin.site.register([Order,OrderDetails])