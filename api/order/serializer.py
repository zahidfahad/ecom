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

    cart_item_count = serializers.SerializerMethodField()
    grand_total = serializers.SerializerMethodField()
    
    class Meta:
        model = Order
        fields = ['id','cart_item_count','grand_total']

    
    def get_cart_item_count(self, obj):
        return obj.get_total_cart_item
    
    def get_grand_total(self, obj):
        return obj.get_order_total_price
    
    def to_representation(self, obj):
        data = super().to_representation(obj)
        order_items = OrderItem.objects.filter(order=obj)
        data['order_items'] = OrderItemSerializer(order_items,many=True).data
        return data
        
