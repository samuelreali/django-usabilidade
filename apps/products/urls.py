from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'products'

router = routers.DefaultRouter()
router.register('produtos', views.ProductViewSet, basename='produtos')

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.list_products, name='list_products'),
    path('adicionar/', views.add_product, name='add_product'),
    path('editar/<int:id_product>/', views.edit_product, name='edit_product'),
    path('excluir/<int:id_product>/', views.delete_product, name='delete_product'),
]