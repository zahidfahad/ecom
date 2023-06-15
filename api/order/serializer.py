from rest_framework import serializers
from order.models import (
    Order,OrderItem
)
from api.product.serializers import(
    ProductSerializer
)


class OrderItemSerializer(serializers.ModelSerializer):
    
    item = ProductSerializer()
    total = serializers.SerializerMethodField()
    class Meta:
        model = OrderItem
        fields = ['id','item','quantity','total']
        
    def get_total(self,obj):
        return obj.get_item_total_price


class CartDetailSerializer(serializers.ModelSerializer):
    
    order_items = serializers.SerializerMethodField()
    cart_item_count = serializers.SerializerMethodField()
    grand_total = serializers.SerializerMethodField()
    
    class Meta:
        model = Order
        fields = ['id','order_items','cart_item_count','grand_total']
        
    def get_order_items(self,obj):
        order_items = OrderItem.objects.filter(order=obj)
        serializer = OrderItemSerializer(order_items,many=True)
        return serializer.data
    
    def get_cart_item_count(self,obj):
        return obj.get_total_cart_item
    
    def get_grand_total(self,obj):
        return obj.get_order_total_price
        
