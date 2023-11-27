from django.shortcuts import render
from .models import Category
from rest_framework import viewsets
from .serializer import CategorySerializer
from django.http import HttpResponse

# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer  
