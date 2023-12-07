from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.list_carts, name='list_carts'),
    path('adicionar/', views.add_cart, name='add_cart'),
    path('pedido/', views.add_order, name='add_order'),
    path('excluir/<int:id_cart>/', views.delete_cart, name='delete_cart'),
]