from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class CartPage(TemplateView):
    template_name = 'order/cart_page.html'
