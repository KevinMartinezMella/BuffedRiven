from django.db import models

# Create your models here.


class Usuario(models.Model):
    nombre = models.CharField(max_length = 50, null = False, blank = False)
    apellido = models.CharField(max_length = 50, null = False, blank = False)
    email = models.CharField(max_length = 255, null = False, blank = False)
    password = models.CharField(max_length = 70, null = False, blank = False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)