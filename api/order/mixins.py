from order.models import (
    Order,OrderItem
)
from products.models import (
    Product
)

from base.exceptions import (
    APIERROR
)

class OrderMixin:
    
    def update_cart(self,order,item,action):
        if action == 'add':
            order_item, created = OrderItem.objects.get_or_create(order=order,item=item)
            order_item.quantity += 1
            order_item.total = order_item.get_item_total_price
            order_item.save()
            
        if action == 'remove':
            order_item, created = OrderItem.objects.get_or_create(order=order,item=item)
            if order_item.quantity > 0:
                order_item.quantity -= 1
                order_item.total = order_item.get_item_total_price
                order_item.save()
            else:
                raise APIERROR(detail={"bad_request": "quanity is already set to 0"})
            
        return order_item
    
    
    def handle_order(self):
        order_data = self.request.data
        item = Product.objects.get(id=order_data['item_id'])
        action = order_data['action']
        if self.request.user.is_authenticated:
            order, created = Order.objects.get_or_create(customer=self.request.user,complete=False)
        else:
            order , created = Order.objects.get_or_create(customer_device=order_data['device'],complete=False)
        order_item = self.update_cart(order,item,action)
        
        data = {
            "item": {
                "id": order_item.item.id,
                "quantity": order_item.quantity,
                "total": order_item.total,
            },
            "grand_total": order.get_order_total_price
        }
        return data
 
 
    def get_order_details(self):
        if self.request.user.is_authenticated:
            order = Order.objects.filter(customer=self.request.user,complete=False).last()
        else:
            order = Order.objects.filter(customer_device=self.request.query_params['device'],complete=False)    
        return order
            
        
        