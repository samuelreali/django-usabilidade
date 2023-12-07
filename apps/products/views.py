from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProductForm
from .models import Product
from rest_framework import viewsets
from .serializer import ProductSerializer
from django.http import HttpResponse

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer  

def add_product(request):
    template_name = 'products/add_product.html'
    context = {}
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('products:list_products')
    form = ProductForm()
    context['form'] = form
    return render(request, template_name, context)

def add_chart(request, id_product):
    Product.objects.filter(id=id_product).update(is_cart=True)
    return redirect('core:home')

def list_products(request):
    template_name = 'products/list_products.html',
    products = Product.objects.filter()
    context = {
        'products': products
    }
    return render(request, template_name, context)

def edit_product(request, id_product):
    template_name = 'products/add_product.html'
    context ={}
    product = get_object_or_404(Product, id=id_product)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES,  instance=product)
        if form.is_valid():
            form.save()
            return redirect('products:list_products')
    form = ProductForm(instance=product)
    context['form'] = form
    return render(request, template_name, context)

def delete_product(request, id_product):
    product = Product.objects.get(id=id_product)
    product.delete()
    return redirect('products:list_products')