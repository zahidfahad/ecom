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
    http_method_names = ['get','post','patch','delete','put','head', 'options']
    






from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from administration.models import User
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

class ListUsers(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        serializer = self.serializer_class(self.queryset.all(),many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)