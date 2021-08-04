from django.shortcuts import render
from rest_framework.response import Response
from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404
from table.models import *
from rest_framework.parsers import JSONParser
from rest_framework import mixins, generics, serializers
from table.serializers import (
    CategoryGetFkObjectSerializer,
    CategorySerializer,
    OrderSerializer,
    RoomGetFkObjectSerializer,
    RoomSerializer,
)

class CatgegoryGenericApiView(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = "id"

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        if id:
            return self.update(request, id)
        return Response({"error": "id not found"})

    def delete(self, request, id=None):
        if id:
            return self.destroy(request, id)
        return Response({"error": "id not found"})


class RoomGenericApiView(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()
    lookup_field = "id"

    def get(self, request, id=None):
        if id:
            queryset = get_object_or_404(Room, id)
            if queryset:
                serializer = RoomGetFkObjectSerializer(queryset, many=False)
                return Response(serializer.data)
            else:
                return Response(
                    {
                        "ok": False,
                        "data": "The information in the id you provided is not available",
                    }
                )
        else:
            queryset = Room.objects.all()
            serializer = RoomGetFkObjectSerializer(queryset, many=True)
            return Response(serializer.data)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        if id:
            return self.update(request, id)
        return Response({"error": "id not found"})

    def delete(self, request, id=None):
        if id:
            return self.destroy(request, id)
        return Response({"error": "id not found"})

class OrderGenericApiView(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    lookup_field = "id"

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        if id:
            return self.update(request, id)
        return Response({"error": "id not found"})

    def delete(self, request, id=None):
        if id:
            return self.destroy(request, id)
        return Response({"error": "id not found"})
