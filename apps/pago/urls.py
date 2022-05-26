from django.urls import path

from . import views


urlpatterns = [
    path('pago', views.pago, name='pago')
]