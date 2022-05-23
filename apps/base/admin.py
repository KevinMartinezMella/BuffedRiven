import imp
from django.contrib import admin
from . models import Division, Usuario, Rango, Servidor, Cuenta

# Register your models here.


admin.site.register(Usuario)
admin.site.register(Rango)
admin.site.register(Servidor)
admin.site.register(Cuenta)
admin.site.register(Division)
