from django.urls import path
from . import views
from cart.views import add_cart, list_carts, delete_cart

app_name = 'core'

urlpatterns = [
    path('', list_carts, name='home'),
    path('adicionar/', add_cart, name='add_cart'),
    path('excluir/<int:id_cart>/', delete_cart, name='delete_cart'),
]