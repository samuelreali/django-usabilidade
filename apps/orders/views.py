from django.shortcuts import render
from .models import Order
from rest_framework import viewsets
from .serializer import OrderSerializer
from django.http import HttpResponse

# Create your views here.
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer  
