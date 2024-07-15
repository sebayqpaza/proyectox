from django.urls import path
from . import views

app_name = 'productos'

urlpatterns = [
    path('', views.lista_zapatillas, name='lista_zapatillas'),
    path('detalle/<int:id>/', views.detalle_zapatilla, name='detalle_zapatilla'),
]
