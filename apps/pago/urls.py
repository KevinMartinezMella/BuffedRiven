from django.urls import path

from . import views


urlpatterns = [
    path('pago', views.pago, name='pago'),
    path('pago-aprobado', views.aprobado, name='aprobado'),
    path('pago-rechazado', views.rechazado, name='rechazado')
]