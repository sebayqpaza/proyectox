from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Carrito
from productos.models import Zapatilla

@login_required(login_url='usuarios:login')
def agregar_al_carrito(request, zapatilla_id):
    zapatilla = get_object_or_404(Zapatilla, id=zapatilla_id)
    carrito, creado = Carrito.objects.get_or_create(usuario=request.user)
    carrito.zapatillas.add(zapatilla)
    return redirect('carrito:ver_carrito')

@login_required(login_url='usuarios:login')
def ver_carrito(request):
    carrito, creado = Carrito.objects.get_or_create(usuario=request.user)
    contexto = {'carrito': carrito}
    return render(request, 'carrito/ver_carrito.html', contexto)

@login_required(login_url='usuarios:login')
def eliminar_del_carrito(request, zapatilla_id):
    zapatilla = get_object_or_404(Zapatilla, id=zapatilla_id)
    carrito = Carrito.objects.get(usuario=request.user)
    carrito.zapatillas.remove(zapatilla)
    return redirect('carrito:ver_carrito')
