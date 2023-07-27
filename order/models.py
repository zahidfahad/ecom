from enum import unique
from django.db import models
from base.models import BaseModel
from administration.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Order(BaseModel):
    customer_device = models.CharField(max_length=150,db_column='customer',verbose_name=_("Device ID"),blank=True,null=True)
    customer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        db_column='customer_id',
        verbose_name=_("CUstomer Account"),
        blank=True,null=True
    )
    complete = models.BooleanField(default=False,db_column='complete',verbose_name=_("Designates whwther this order is complete or not"))
    cancel = models.BooleanField(default=False,db_column='cancel',verbose_name=_("Designates whether order is cancelled or not"))
    
    def __str__(self):
        return self.customer.username if self.customer else self.customer_device
    
    
    @property
    def get_order_total_price(self):
        order_items = self.items.all()
        return sum([item.get_item_total_price for item in order_items])
    
    @property
    def get_total_cart_item(self):
        return sum([item.quantity for item in self.items.all()])
    
    def save(self, *args, **kwargs):
        if not all(v is True for v in[self.complete,self.cancel]):
            return super(Order, self).save(*args,**kwargs)
    
    
class OrderItem(BaseModel):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,db_column='order_id',verbose_name=_("Order"),related_name="items")
    item = models.ForeignKey('products.Product',on_delete=models.PROTECT,db_column='item_id',verbose_name=_("Order Item"))
    quantity = models.PositiveIntegerField(db_column='quantity',default=0,verbose_name=_("Quantity"))
    total = models.PositiveIntegerField(verbose_name=_("Item Total Price"),db_column='total',null=True)
    
    def __str__(self) -> str:
        return str(self.order.complete)
    
    @property
    def get_item_total_price(self):
        return self.quantity * self.item.get_price
    
    
class Shipping(BaseModel):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,db_column='order_id',verbose_name=_("Order"),related_name="shipping")
    address = models.CharField(max_length=1000,db_column='address',verbose_name=_("Address"))
    receiver_name = models.CharField(max_length=50,db_column='receiver_name',verbose_name=_("Reciever Name"))
    receiver_contact = models.CharField(max_length=15,db_column='receiver_contact',verbose_name=_("Receiver Contact"))


class OrderStatus(BaseModel):
    from .configs.choices import OrderStatus
    
    order = models.ForeignKey(Order,on_delete=models.CASCADE,db_column='order_id')
    status = models.CharField(max_length=50,db_column='delivery_status',choices=OrderStatus.choices,default=OrderStatus.NEW)
    
    
    def __str__(self):
        self.status
        
    class Meta:
        unique_together = ('order','status')
