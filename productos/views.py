from django.shortcuts import render, get_object_or_404
from .models import Zapatilla

def lista_zapatillas(request):
    zapatillas = Zapatilla.objects.all()
    return render(request, 'productos/lista_zapatillas.html', {'zapatillas': zapatillas})

def detalle_zapatilla(request, id):
    zapatilla = get_object_or_404(Zapatilla, id=id)
    return render(request, 'productos/detalle_zapatilla.html', {'zapatilla': zapatilla})
