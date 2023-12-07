from django.shortcuts import render, get_object_or_404, redirect
from .forms import CartForm
from orders.forms import OrderForm
from .models import Cart
from products.models import Product
from django.db.models import Sum
from django.contrib import messages

# Create your views here.

def add_cart(request):
    template_name = 'cart/add_cart.html'
    context = {}
    if request.method == 'POST':
        form = CartForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('core:home')
    form = CartForm()
    context['form'] = form
    return render(request, template_name, context)

def list_carts(request):
    template_name = 'cart/list_cart.html'
    carts = Product.objects.filter()
    context = {
        'carts': carts
    }
    return render(request, template_name, context)

# def edit_cart(request, id_product):
#     template_name = 'carts/add_cart.html'
#     context ={}
#     product = get_object_or_404(Cart, id=id_product)
#     if request.method == 'POST':
#         form = CartForm(request.POST, request.FILES,  instance=product)
#         if form.is_valid():
#             form.save()
#             return redirect('carts:list_carts')
#     form = CartForm(instance=cart)
#     context['form'] = form
#     return render(request, template_name, context)

def delete_cart(request, id_cart):
    Product.objects.filter(id=id_cart).update(is_cart=False)
    return redirect('cart:list_carts')

def add_order(request):
    total_price = Product.objects.filter(is_cart=True).aggregate(Sum('price'))['price__sum']
    total_price = total_price or 0
    if(total_price != 0):
        Product.objects.all().update(is_cart=False)
        messages.success(request, ("Pedido efetuado com sucesso! Valor: R$"+ str(total_price)))
        return redirect('core:home')
    else:
        messages.success(request, ("Adicione produtos ao seu carrinho antes de finalizar o pedido!"))
        return redirect('core:home')