from django.urls import path
from .views import *

urlpatterns = [

    path("categoryapi/", CatgegoryGenericApiView.as_view(), name="categoryapi"),
    path("roomapi/", RoomGenericApiView.as_view(), name="orderapi"),
    path("orderapi/", OrderGenericApiView.as_view(), name="orderapi"),

    path("categoryapi/<int:id>", CatgegoryGenericApiView.as_view()),
    path("roomapi/<int:id>", RoomGenericApiView.as_view()),
    path("orderapi/<int:id>", OrderGenericApiView.as_view()),
]