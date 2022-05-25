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
        for key, valor in carro.items():
            context = {
                'email': email,
                'precio' : valor['acumulador'],
                'servidor' : valor['servidor_cuenta'],
                'tipo_cuenta' : valor['tipo_cuenta'],
                'cantidad' : valor['cantidad'],
            }
            # Se renderiza el template y se envias parametros
            content = template.render(context)
        print(carro)
            # Se crea el correo (titulo, mensaje, emisor, destinatario)
        msg = EmailMultiAlternatives('Gracias por tu compra','Comprobante de compra', settings.EMAIL_HOST_USER, [email])

        msg.attach_alternative(content, 'text/html')
        if msg.send():
            print('envio')
        else:
            print('no envio')
        return redirect('/')
