from rest_framework import viewsets,filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db import transaction
from datetime import datetime, timezone, timedelta
from django.http import Http404

from products.models import (
    Category,SubCategory,
    Product
)
from .serializers import(
    CategorySerializer,
    SubCategorySerializer,
    ProductSerializer
)


class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = []
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]

    ordering_fields = ['id','-created_at']
    filterset_fields = []
    search_fields = ['name','id']
    http_method_names = ['get','post','patch','delete','put','head']
    
    
    def get_serializer_class(self):
        if self.action == 'get_sub_categories':
            return SubCategorySerializer
        return self.serializer_class
    
    
    @action(detail=False, methods=['get'], url_path='related-sub-categories')
    def get_sub_categories(self, request, *args, **kwargs):
        category_id = request.query_params.get('category_id')
        sub_categories = SubCategory.objects.filter(category_id=category_id)[:20]
        return Response(self.get_serializer(sub_categories,many=True).data)
    
    
    
class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.select_related("category","sub_category").all()
    serializer_class = ProductSerializer
    permission_classes = []
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]

    ordering_fields = ['id','-created_at']
    filterset_fields = ['category','sub_category']
    search_fields = ['category','sub_category','id','title']
    http_method_names = ['get','post','patch','delete','put','head']
        