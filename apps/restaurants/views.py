from django.shortcuts import render
from .models import Restaurant
from rest_framework import viewsets
from .serializer import RestaurantSerializer
from django.http import HttpResponse

# Create your views here.
class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer  
