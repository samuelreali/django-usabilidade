from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('excluir/<int:id_cart>/', views.delete_cart, name='delete_cart'),
]