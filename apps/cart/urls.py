from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.list_carts, name='list_carts'),
    path('adicionar/', views.add_cart, name='add_cart'),
    path('editar/<int:id_cart>/', views.edit_cart, name='edit_cart'),
    path('excluir/<int:id_cart>/', views.delete_cart, name='delete_cart'),
]