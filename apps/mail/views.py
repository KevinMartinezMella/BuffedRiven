from django.shortcuts import redirect, render
from django.conf import settings
from django.views import View
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives


class Send(View):
    def envio_correo(email, lista):
        template = get_template('mail/mail-aprobado.html')
        context = {
            'email': email,
            'contenido': lista
        }
        # Se renderiza el template y se envias parametros
        content = template.render(context)
            # Se crea el correo (titulo, mensaje, emisor, destinatario)
        msg = EmailMultiAlternatives('Gracias por tu compra','Comprobante de compra', settings.EMAIL_HOST_USER, [email])

        msg.attach_alternative(content, 'text/html')
        
        msg.send()