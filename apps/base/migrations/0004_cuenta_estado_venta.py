# Generated by Django 4.0.4 on 2022-05-26 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_rango_precio_cuenta'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuenta',
            name='estado_venta',
            field=models.IntegerField(default=0, null=True),
        ),
    ]