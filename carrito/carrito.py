
class Carrito:
    def __init__(self, request):
        self.session = request.session
        carrito = self.session.get('carrito')
        if not carrito:
            carrito = self.session['carrito'] = {}
        self.carrito = carrito

    def add(self, zapatilla):
        zapatilla_id = str(zapatilla.id)
        if zapatilla_id not in self.carrito:
            self.carrito[zapatilla_id] = {'precio': str(zapatilla.precio)}
        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, zapatilla):
        zapatilla_id = str(zapatilla.id)
        if zapatilla_id in self.carrito:
            del self.carrito[zapatilla_id]
            self.save()