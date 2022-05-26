from django.shortcuts import render, redirect
import mercadopago


def pago(request):
    if request.session['carro'] != {}:
        sdk = mercadopago.SDK("ACCESS_TOKEN")
        carro = request.session["carro"]
        lista = []
        for key, valor in carro.items():
            context = {
                'title' : valor['tipo_cuenta'],
                'unit_price' : int(valor['precio']),
                'quantity' : int(valor['cantidad']),
                'currency_id': 'CLP',
            }
            lista.append(context)
        print(lista)
        datos_preferencia = {
            "items": lista,
            "back_urls": {
                "success": "https://www.success.com",
                "failure": "http://www.failure.com",
                "pending": "http://www.pending.com"
            },
            "auto_return": "approved",
            "binary_mode": True,
        }

        respuesta_preferencia = sdk.preference().create(datos_preferencia)
        preferencia = respuesta_preferencia["response"]
        return render(request, 'pago.html', {'preferencia' : preferencia})
    else:
        return redirect('/')
