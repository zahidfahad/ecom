from django.urls import path
from .views import *


urlpatterns = [
    path('cart/', CartPage.as_view(), name = 'CartPage'),
    path('checkout/', CheckoutPage.as_view(), name = 'CheckoutPage'),
]
