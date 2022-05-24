def total_carro(request):
    total = 0
    carro = request.session.get('carro')
    if "carro" in request.session.keys():
        for key, valor in request.session["carro"].items():
            total += int(valor['acumulador'])

    return {'total_carro' : total}