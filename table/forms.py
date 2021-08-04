from django import forms
from django.forms import fields
from .models import Order, Room
from django.conf import settings



class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"
        rooms = Room.objects.all()
        choices = []
        for room in rooms:
            choices.append((room.room_number, room.room_number))

        # widgets = {
        #     "room": forms.Select(attrs={ "class": "form-control"}, choices=choices),
        #     "start_date": forms.DateInput(attrs={"type": "date", "class": "form-control", }),
        #     "finish_date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
        #     "first_name": forms.TextInput(attrs={"type": "text", "placeholder": "First Name", "class": "form-control"}),
        #     "last_name": forms.TextInput(attrs={"type": "text", "placeholder": "Last Name", "class": "form-control"}),
        #     "phone_number": forms.TextInput(attrs={"type": "text", "placeholder": "Phone number", "class": "form-control"}),
        #     "order_cost": forms.NumberInput(attrs={"type": "number", "disabled": "True", "placeholder": "Cost", "class": "form-control"}),
        # }
        


