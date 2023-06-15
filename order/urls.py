from django.urls import path
from .views import *


urlpatterns = [
    path('cart-page/', CartPage.as_view(), name = 'CartPage'),
]
