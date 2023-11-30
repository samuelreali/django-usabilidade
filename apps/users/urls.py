from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'users'

router = routers.DefaultRouter()

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.findUsers, name='list_products'),
    path('adicionar/', views.add_user, name='add_user'),
   # path('editar/<int:id_product>/', views.edit_product, name='edit_product'),
   # path('excluir/<int:id_product>/', views.delete_product, name='delete_product'),
]