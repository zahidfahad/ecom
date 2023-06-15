from rest_framework import viewsets,filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db import transaction
from datetime import datetime, timezone, timedelta
from django.http import Http404

from home.models import (
    Banner
)
from .serializers import (
    BannerSerializer
)



class BannerViewset(viewsets.ModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
    permission_classes = []
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]

    ordering_fields = ['id','-created_at']
    filterset_fields = []
    search_fields = ['id']
    http_method_names = ['get','post','patch','delete','put','head']
    
        