from django.urls import path
from . import views
from cart.views import add_cart, list_carts, delete_cart
from users.views import login_user

app_name = 'core'

urlpatterns = [
    path('', views.home, name="home"),
    path('carrinho/', list_carts, name='cart'),
    path('adicionar/', add_cart, name='add_cart'),
    path('excluir/<int:id_cart>/', delete_cart, name='delete_cart'),
]