from django import forms
from .models import Shipping



class ShippingForm(forms.ModelForm):
    class Meta:
        model = Shipping
        fields= ['address', 'receiver_name', 'receiver_contact']