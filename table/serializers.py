from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Category, Room, Order

# class CategorySerializer(serializers.Serializer):
#     category = serializers.CharField(max_length = 50)
#     price = serializers.IntegerField()

#     def create(self, validated_data):
#         return Category.objects.create(validated_data)

#     def update(self, instance, validated_data):
#         instance.category = validated_data.get("category", instance.category)
#         instance.price = validated_data.get("price", instance.price)
#         instance.save()
#         return instance

# class RoomSerializer(serializers.Serializer):
#     room_number = serializers.IntegerField()
#     person_number = serializers.IntegerField()
#     floor = serializers.CharField(max_length=64)
#     category = serializers.ForeignKey(Category, on_delete=models.CASCADE)

#     def create(self, validated_data):
#         return Room.objects.create(validated_data)

#     def update(self, instance, validated_data):
#         instance.category = validated_data.get("category", instance.category)
#         instance.price = validated_data.get("price", instance.price)
#         instance.save()
#         return instance

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

