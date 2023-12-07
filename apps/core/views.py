from django.shortcuts import render
from products.models import Product

# Create your views here.
def home(request):
    template_name ='core/home.html'
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, template_name, context)