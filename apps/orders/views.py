from django.shortcuts import render
from .models import Order
from products.models import Product
from django.db.models import Sum
from rest_framework import viewsets
from .serializer import OrderSerializer
from django.http import HttpResponse

# Create your views here.
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer  

def list_orders(request):
    template_name = 'orders/list_orders.html',
    orders = Order.objects.filter()
    # Obtém a soma de todos os preços onde mark_as é True
    total_price = Product.objects.filter(is_cart=True).aggregate(Sum('price'))['price__sum']
    total_price = total_price or 0
    context = {
        'orders': orders,
        'total_price': total_price
    }
    return render(request, template_name, context)