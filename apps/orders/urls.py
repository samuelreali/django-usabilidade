from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'ordens'

router = routers.DefaultRouter()
router.register('ordens', views.OrderViewSet, basename='ordens')

urlpatterns = [
    path('', views.list_orders, name='list_orders'),
]