from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Category, Room, Order




class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class CategoryGetFkObjectSerializer(serializers.ModelSerializer):
    room = RoomSerializer()

    class Meta:
        model = Category
        fields = "__all__"

class RoomGetFkObjectSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    
    class Meta:
        model = Room
        fields = "__all__"

