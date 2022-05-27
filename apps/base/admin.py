from django.contrib import admin
from . models import Division, Precio, Rango, Servidor, Cuenta

admin.site.register(Rango)
admin.site.register(Servidor)
admin.site.register(Cuenta)
admin.site.register(Division)
admin.site.register(Precio)
