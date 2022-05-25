from django . urls import path
from . import views

urlpatterns = [
    path('send/', views.Send.as_view(), name='send'),
]