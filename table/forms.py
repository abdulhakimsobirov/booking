from django import forms
from django.forms import fields
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"

        widgets = {
            "room": forms.DateInput(attrs={ "class": "form-control", "disabled": "True"}),
            "start_date": forms.DateInput(attrs={"type": "text", "class": "form-control"}),
            "finish_date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "first_name": forms.TextInput(attrs={"type": "text", "class": "form-control"}),
            "last_name": forms.TextInput(attrs={"type": "text", "class": "form-control"}),
            "phone_number": forms.TextInput(attrs={"type": "text", "class": "form-control"}),
            "order_cost": forms.NumberInput(attrs={"type": "number", "class": "form-control"}),
        }


