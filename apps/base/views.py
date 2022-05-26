from django.shortcuts import redirect, render
from apps.base.models import Cuenta
from apps.base.carro import Carro

def index(request):
    return render(request, 'index.html')

def gold(request):
    cuenta_platino = Cuenta.objects.filter(rango = 6)
    cuenta_oro = Cuenta.objects.filter(rango = 5)
    cuenta_unranked = Cuenta.objects.filter(rango = 1)
    context = {
        'cuenta_unranked': cuenta_unranked,
        'cuenta_oro' : cuenta_oro,
        'cuenta_platino' : cuenta_platino
    }
    return render(request, 'cuentas.html', context)

def agregar_cuenta(request, idCuenta):
    carro = Carro(request)
    cuenta = Cuenta.objects.get(id = idCuenta)
    carro.agregar(cuenta)
    return redirect('oro')

def eliminar_cuenta(request, idCuenta):
    carro = Carro(request)
    cuenta = Cuenta.objects.get(id = idCuenta)
    carro.quitar(cuenta)
    return redirect('oro')

def restar_cuenta(request, idCuenta):
    carro = Carro(request)
    cuenta = Cuenta.objects.get(id = idCuenta)
    carro.decrementar(cuenta)
    return redirect('oro')

def limpiar_cuenta(request):
    carro = Carro(request)
    carro.vaciar()
    return redirect('oro')