# Generated by Django 4.0.4 on 2022-05-23 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_precio'),
    ]

    operations = [
        migrations.AddField(
            model_name='rango',
            name='precio_cuenta',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.precio'),
        ),
    ]
