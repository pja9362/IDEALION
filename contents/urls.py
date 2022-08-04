from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('<str:content_id>',detailPlace, name = "detailPlace"),
    path('addPlace/', addPlace, name = "addPlace"),
    path('create/', create, name = "create"),
    path('editPlace/<str:content_id>', editPlace, name="editPlace"),
    path('updatePlace/<str:content_id>', updatePlace, name = "updatePlace"),
    path('delete/<str:content_id>', deletePlace, name = "deletePlace"),
    path('myMap/<str:Category>', myMap, name = "myMap"),
    path('newCategory/', newCategory, name = "newCategory"),
    path('ourMap/', ourMap, name="ourMap"),
    path('showtoilets/', showtoilets, name="showtoilets"),
    path('showsmokings/', showsmokings, name="showsmokings"),
]
