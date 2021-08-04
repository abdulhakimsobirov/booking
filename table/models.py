from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=50)
    


    def __str__(self):
        return self.category

class Room(models.Model):
    room_number = models.IntegerField()
    person_number = models.IntegerField()
    floor = CharField(max_length=64)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"room{str(self.room_number)}"


class Order(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_date = models.DateField()
    finish_date = models.DateField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=14)
    create_date = models.DateField(auto_now_add=True)
    order_cost = models.IntegerField()


    def __str__(self):
        return f"{self.phone_number} - {self.first_name}"

