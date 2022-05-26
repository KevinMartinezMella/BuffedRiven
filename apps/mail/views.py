from django.shortcuts import redirect, render
from django.conf import settings
from django.views import View
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives


class Send(View):
    def get(self, request):
        if request.session['carro'] != {}:
            return render(request, 'mail/send.html')
        else:
            return redirect('/')
    
    def post(self, request):
        email = request.POST.get('email')
        carro = request.session["carro"]
        template = get_template('mail/mail-aprobado.html')
        total = 0
        cantidad = 0
        for key, valor in carro.items():
            total = total + valor['acumulador']
            cantidad = cantidad + valor['cantidad']
            context = {
                'email': email,
                'precio' : valor['acumulador'],
                'tipo_cuenta' : valor['tipo_cuenta'],
                'cantidad' : valor['cantidad'],
                'total': total,
                'cantidad_total' : cantidad
            }
            # Se renderiza el template y se envias parametros
            content = template.render(context)
            # Se crea el correo (titulo, mensaje, emisor, destinatario)
        msg = EmailMultiAlternatives('Gracias por tu compra','Comprobante de compra', settings.EMAIL_HOST_USER, [email])

        msg.attach_alternative(content, 'text/html')
        return redirect('/')
