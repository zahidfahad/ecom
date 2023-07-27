from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import (
    ShippingForm,
)
# Create your views here.


class CartPage(TemplateView):
    template_name = 'order/cart_page.html'
    
class CheckoutPage(TemplateView):
    template_name = 'order/checkout_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = ShippingForm()
        return context
    