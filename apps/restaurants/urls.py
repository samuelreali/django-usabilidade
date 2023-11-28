from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'restaurants'

router = routers.DefaultRouter()
router.register('restaurantes', views.RestaurantViewSet, basename='restaurantes')

urlpatterns = [
    path('', include(router.urls) )
]