from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def registro(request):
    return render(request, 'registro.html')

def login(request):
    return render(request, 'iniciosesion.html')

def cuentas(request):
    return render(request, 'cuentas.html')