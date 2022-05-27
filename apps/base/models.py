from __future__ import division
from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length = 50, null = False, blank = False)
    apellido = models.CharField(max_length = 50, null = False, blank = False)
    email = models.CharField(max_length = 255, null = False, blank = False)
    password = models.CharField(max_length = 70, null = False, blank = False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f'{self.nombre}'

    class Meta:
        db_table = 'usuario'


class Division(models.Model):
    numero_division = models.CharField(max_length = 10, null = True)

    def __str__(self):
            return f'{self.numero_division}'

    class Meta:
        db_table = 'division'


class Precio(models.Model):
    precio = models.IntegerField(null = True)
    
    def __str__(self):
            return f'{self.precio}'

    class Meta:
        db_table = 'precio'


class Rango(models.Model):
    nombre_rango = models.CharField(max_length = 255, null = False)
    precio_cuenta = models.ForeignKey(Precio, on_delete = models.CASCADE, null = True)
    
    def __str__(self):
            return f'{self.nombre_rango} - {self.precio_cuenta}'

    class Meta:
        db_table = 'rango'


class Servidor(models.Model):
    nombre_servidor = models.CharField(max_length = 255, null = False)

    def __str__(self):
        return f'{self.nombre_servidor}'

    class Meta:
        db_table = 'servidor'


class Cuenta(models.Model):
    nombre_usuario = models.CharField(max_length = 50, null = False)
    password = models.CharField(max_length = 70, null = False)
    nivel = models.IntegerField(null = False)
    escencia = models.IntegerField(null = True)
    estado_venta = models.IntegerField(null = True, default=0)
    rango = models.ForeignKey(Rango, on_delete = models.PROTECT)
    division = models.ForeignKey(Division, null = True, on_delete = models.PROTECT)
    servidor = models.ForeignKey(Servidor, on_delete = models.PROTECT)

    def __str__(self):
        return f'{self.nombre_usuario} - {self.password} - {self.servidor.nombre_servidor}'

    class Meta:
        db_table = 'cuenta'