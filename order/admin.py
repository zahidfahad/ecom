from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass



@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    pass


