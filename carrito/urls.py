from django.urls import path
from . import views

app_name = 'carrito'

urlpatterns = [
    path('agregar/<int:zapatilla_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('ver/', views.ver_carrito, name='ver_carrito'),
    path('eliminar/<int:zapatilla_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('finalizar_compra/', views.finalizar_compra, name='finalizar_compra'),
]
