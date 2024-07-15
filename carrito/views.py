from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
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
    contexto = {
        'carrito': carrito
    }
    return render(request, 'carrito/ver_carrito.html', contexto)

@login_required(login_url='usuarios:login')
def eliminar_del_carrito(request, zapatilla_id):
    zapatilla = get_object_or_404(Zapatilla, id=zapatilla_id)
    carrito = Carrito.objects.get(usuario=request.user)
    carrito.zapatillas.remove(zapatilla)
    return redirect('carrito:ver_carrito')

@login_required(login_url='usuarios:login')
def finalizar_compra(request):
    if request.method == 'POST':
        nombre = request.POST.get('name')
        correo_electronico = request.POST.get('email')
        direccion = request.POST.get('address')
        telefono = request.POST.get('phone')
        metodo_pago = request.POST.get('payment_method')

        # mensaje = f'Nombre: {nombre}\nCorreo Electrónico: {correo_electronico}\nDirección: {direccion}\nTeléfono: {telefono}\nMétodo de Pago: {metodo_pago}'
        # send_mail(
        #     'Confirmación de Compra',
        #     mensaje,
        #     settings.DEFAULT_FROM_EMAIL,
        #     [correo_electronico],
        #     fail_silently=False,
        # )

        carrito = Carrito.objects.get(usuario=request.user)
        carrito.zapatillas.clear()

        # Redirecciona a la página de compra exitosa
        return redirect('carrito:compra_exitosa')

    return redirect('carrito:ver_carrito')

def compra_exitosa(request):
    return render(request, 'carrito/compra_exitosa.html')