from rest_framework import serializers
from products.models import (
    Category,SubCategory,
    Product
)



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']
        

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['id','name']
        
        
class ProductSerializer(serializers.ModelSerializer):
    
    price = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = '__all__'
        
        
    def get_price(self,obj):
        return obj.get_price