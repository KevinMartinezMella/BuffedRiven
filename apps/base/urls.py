from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('accounts', views.gold, name='oro'),
    path('agregarcuenta/<int:idCuenta>/', views.agregar_cuenta, name='agregarCuenta'),
    path('eliminarcuenta/<int:idCuenta>/', views.eliminar_cuenta, name='eliminarCuenta'),
    path('restarcuenta/<int:idCuenta>/', views.restar_cuenta, name='restarCuenta'),
    path('limpiarcuenta/', views.limpiar_cuenta, name='limpiarCuenta'),
]