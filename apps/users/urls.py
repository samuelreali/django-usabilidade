from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'users'

router = routers.DefaultRouter()

urlpatterns = [
    path('login_user/', views.login_user, name='login'),
    path('logout_user', views.logout_user, name='logout'),
    path('api/', include(router.urls)),
    path('', views.list_users, name='list_users'),
    path('adicionar/', views.add_user, name='add_user'),
    path('excluir/<int:id_user>/', views.delete_user, name='delete_user'),
    path('editar/<int:id_user>/', views.edit_user, name='edit_user'),
]