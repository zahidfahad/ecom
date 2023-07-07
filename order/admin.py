from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer_device','customer','complete','cancel']



@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order','item','quantity','total']


