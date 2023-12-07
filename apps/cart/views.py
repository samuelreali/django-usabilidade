from django.shortcuts import render, get_object_or_404, redirect
from .forms import CartForm
from .models import Cart
from products.models import Product

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
    cart = Cart.objects.get(id=id_cart)
    cart.delete()
    return redirect('core:home')
