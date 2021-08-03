from rest_framework.response import Response
from table.forms import OrderForm
from django.shortcuts import redirect, render
import datetime
from datetime import date, timedelta
from django.shortcuts import get_object_or_404
from .models import *
from rest_framework.parsers import JSONParser
from rest_framework import mixins, generics, serializers
from .serializers import CategoryGetFkObjectSerializer, CategorySerializer, OrderSerializer, RoomGetFkObjectSerializer, RoomSerializer



today = date.today()
D = timedelta(days=10)
n = today - D
future = []
days = []


for add in range(31):
    o = timedelta(days=add)
    w = n + o
    future.append(w.strftime('%d/%m/%Y'))

print(future)
#     w.strftime('%d/%m/%Y')
#     days.append(w)
# print(days)

# for day in future:
#     days.append(day.split(","))


# day = (datetime.datetime.strptime(i, "%d-%m-%Y") for i in days)
# print(day)

def table(request):
    cat = Category.objects.all()

    orderform = OrderForm()

    if request.method == "POST":
        orderform = OrderForm(request.POST)
        if orderform.is_valid():
            orderform.save()
            return redirect("table")

    return render(request, "table/table.html", {"cat": cat, "day": future, "orderform": orderform})

def order_cost():
    pass


class CatgegoryGenericApiView(generics.GenericAPIView, 
                                mixins.ListModelMixin, 
                                mixins.CreateModelMixin,
                                mixins.UpdateModelMixin,
                                mixins.RetrieveModelMixin,
                                mixins.DestroyModelMixin):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = "id"

    def get(self, request, id = None):
        if id:
            return self.retrieve(request)
        else: 
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id = None):
        if id:
            return self.update(request, id)
        return Response({"error":'id not found'})

    def delete(self, request, id = None):
        if id:
            return self.destroy(request, id)
        return Response({"error": "id not found"})


class RoomGenericApiView(generics.GenericAPIView, 
                                mixins.ListModelMixin, 
                                mixins.CreateModelMixin,
                                mixins.UpdateModelMixin,
                                mixins.RetrieveModelMixin,
                                mixins.DestroyModelMixin):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()
    lookup_field = "id"

    def get(self, request, id = None):
        # if id:
        #     return self.retrieve(request)
        # else: 
        #     return self.list(request)

       
        if id:
            queryset = get_object_or_404(Room, id)
            if queryset:
                serializer = RoomGetFkObjectSerializer(queryset, many=False)
                return Response(serializer.data)
            else:
                return Response({"ok": False, 'data': "The information in the id you provided is not available"})
        else:
            queryset = Room.objects.all()
            serializer = RoomGetFkObjectSerializer(queryset, many=True)
            return Response(serializer.data)

    def post(self, request):
        return self.create(request)

    def put(self, request, id = None):
        if id:
            return self.update(request, id)
        return Response({"error":'id not found'})
    def delete(self, request, id = None):
        if id:
            return self.destroy(request, id)
        return Response({"error": "id not found"})
class OrderGenericApiView(generics.GenericAPIView, 
                                mixins.ListModelMixin, 
                                mixins.CreateModelMixin,
                                mixins.UpdateModelMixin,
                                mixins.RetrieveModelMixin,
                                mixins.DestroyModelMixin):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    lookup_field = "id"

    def get(self, request, id = None):
        if id:
            return self.retrieve(request)
        else: 
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id = None):
        if id:
            return self.update(request, id)
        return Response({"error":'id not found'})

    def delete(self, request, id = None):
        if id:
            return self.destroy(request, id)
        return Response({"error": "id not found"})    

    

