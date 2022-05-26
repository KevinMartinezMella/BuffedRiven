from django.shortcuts import render, redirect
import mercadopago


def pago(request):
    if request.method == "POST":
        link = request.POST.get('link_pago')
        correo = request.POST.get('correo_cliente')
        request.session['correo_usuario'] = correo
        return redirect(link)
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
                "success": "http://127.0.0.1:8000/payments/pago-aprobado",
                "failure": "http://127.0.0.1:8000/payments/pago-rechazado",
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


def aprobado(request):
    status = request.GET.get('status')
    id_pago = request.GET.get('payment_id')
    tipo_pago = request.GET.get('payment_type')
    id_orden = request.GET.get('merchant_order_id')
    if status:
        if status == 'approved':
            context = {
                'status':status,
                'id_pago':id_pago,
                'tipo_pago':tipo_pago,
                'id_orden':id_orden,
            }
            return render(request, 'pagos/pago-aprobado.html', context)
        else:
            return redirect('/')
    else:
        return redirect('/')

def rechazado(request):
    status = request.GET.get('status')
    id_pago = request.GET.get('payment_id')
    tipo_pago = request.GET.get('payment_type')
    id_orden = request.GET.get('merchant_order_id')
    if status:
        if status == 'rejected':
            del request.session['correo_usuario']
            context = {
                'status':status,
                'id_pago':id_pago,
                'tipo_pago':tipo_pago,
                'id_orden':id_orden,
            }
            return render(request, 'pagos/pago-rechazado.html', context)
        else:
            return redirect('/')
    else:
        return redirect('/')