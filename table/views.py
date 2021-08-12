from rest_framework.response import Response
from table.forms import OrderForm
from django.shortcuts import redirect, render
import datetime
from datetime import date, timedelta
from django.shortcuts import get_object_or_404
from .models import *
from rest_framework.parsers import JSONParser
from rest_framework import mixins, generics, serializers
from .serializers import (
    CategoryGetFkObjectSerializer,
    CategorySerializer,
    OrderSerializer,
    RoomGetFkObjectSerializer,
    RoomSerializer,
)


today = date.today()
D = timedelta(days=10)
n = today - D
future = []
days = []


for add in range(31):
    o = timedelta(days=add)
    w = n + o
    future.append(w.strftime("%d/%m/%Y"))


f = future[0][3:5]
first_month = [f"{int(f)}", 0]
second_month = [f"{int(f)+1}", 0]
for item in future:
    
    if f == item[3:5]:
        first_month[1] += 1
    else:
        second_month[1] += 1


def table(request):
    cat = Category.objects.all()

    orderform = OrderForm()

    if request.method == "POST":
        orderform = OrderForm(request.POST)
        print(orderform)
        if orderform.is_valid():
            orderform.save()
            print("1111111111111111111")
            return redirect("table")
            

    return render(
        request,
        "table/index.html",
        {
            "cat": cat,
            "day": future,
            "orderform": orderform,
            "second_month": second_month,
            "first_month": first_month,
        },
    )


def order_cost():
    pass



