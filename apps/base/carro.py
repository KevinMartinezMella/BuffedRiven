class Carro:

    def __init__(self, request):
        self.request = request
        self.session = request.session
        carro = self.session.get('carro')

        if not carro:
            carro = self.session['carro'] = {}
        
        self.carro = carro

    def agregar(self, cuenta):
        if str(cuenta.id) not in self.carro.keys():
            self.carro[cuenta.id] = {
                'id_cuenta' : cuenta.id,
                'tipo_cuenta' : cuenta.rango.nombre_rango,
                'servidor_cuenta' : cuenta.servidor.nombre_servidor,
                'cantidad' : 1,
                'precio': cuenta.rango.precio_cuenta.precio,
                'acumulador' : cuenta.rango.precio_cuenta.precio,
            }
        else:
            for key, valor in self.carro.items():
                if key == str(cuenta.id):
                    valor['cantidad'] = valor['cantidad'] + 1
                    valor['acumulador'] += valor['precio']
                    break
        self.guardar()

    def quitar(self, cuenta):
        id_cuenta = str(cuenta.id)
        if id_cuenta in self.carro:
            del self.carro[id_cuenta]
        self.guardar()

    def decrementar(self, cuenta):
        for key, valor in self.carro.items():
            if key == str(cuenta.id):
                valor['cantidad'] = valor['cantidad'] - 1
                valor['acumulador'] -= valor['precio']
                self.guardar()
                if valor['cantidad'] < 1:
                    self.quitar(cuenta)
                break
            else:
                print("El producto no existe en el carro")

    def vaciar(self):
        self.session['carro'] = {}
        self.session.modified = True

    def guardar(self):
        self.session['carro'] = self.carro
        self.session.modified = True