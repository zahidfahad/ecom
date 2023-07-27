from rest_framework import viewsets,filters
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db import transaction
from datetime import datetime, timezone, timedelta
from django.http import Http404
from order.models import (
    Order,OrderItem,
    Shipping
)
from .serializer import (
    CartDetailSerializer,
)
from .mixins import OrderMixin



class OrderViewset(viewsets.ModelViewSet,OrderMixin):
    queryset = Order.objects.all()
    serializer_class = None
    permission_classes = []
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]

    ordering_fields = ['id','-created_at']
    filterset_fields = ['customer__username']
    search_fields = ['customer_device','id','customer__username']
    http_method_names = ['post']
    
    
    def create(self, request, *args, **kwargs):
        with transaction.atomic():
            data = self.handle_order()
        return Response(data)
        


class CartDetails(APIView,OrderMixin):
    serializer_class = CartDetailSerializer 
    
    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.get_order_details(),context={"request": request})
        return Response(serializer.data)
    
    
    
class CheckoutViewset(viewsets.ModelViewSet):
    pass